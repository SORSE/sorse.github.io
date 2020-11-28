import requests
import os
import sys
import json
from argparse import ArgumentParser
from dotenv import load_dotenv
import frontmatter
import logging
from pathlib import Path
import subprocess
from io import BytesIO
from shutil import copyfile

# original porkflow 
# A new branch is generated on the website repository
# For each new contribution (regular or invited), a new upload is triggered via https://zenodo.org/deposit/new?c=sorse
# contents for the form are copied from the corresponding markdown files
# Upload type: Publication
# Publication type: Conference Paper
# Publication date: The date that is published in the yaml Frontmatter of the markdown-file.
# Description: The abstract of the contribution
# A DOI is reserved by clicking the  button. DO NOT SUBMIT THIS FORM UNTIL THE VERY END OF THIS WORKFLOW!
# Edit the markdown-file of the branch in step 1 and add the doi to the yaml frontmatter, e.g. via doi: 10.5281/zenodo.3977886
# Commit the changes for the markdown-file
# If necessary, repeat step 2-6 for other events
# Create a PR from the branch in step 1 into the master branch
# Start the generate-pdfs workflow for the selected branch on Github and wait until it’s finished (it opens a PR)
# Merge the PR from step 9
# Merge the PR from step 8
# Delete the branch from step 9
# delete the branch from step 8
# Add the new PDF for each contribution (that now shows the DOI) to the open form on zenodo
# Submit the form
# Accept the contribution. FT

# Response Codes
# 200 OK Request succeeded. Response included. Usually sent for GET/PUT/PATCH requests.
# 201 Created Request succeeded. Response included. Usually sent for POST requests.
# 202 Accepted Request succeeded. Response included. Usually sent for POST requests, where background processing is needed to fulfill the request.
# 204 No Content Request succeeded. No response included. Usually sent for DELETE requests.
# 400 Bad Request Request failed. Error response included.
# 401 Unauthorized Request failed, due to an invalid access token. Error response included.
# 403 Forbidden Request failed, due to missing authorization (e.g. deleting an already submitted upload or missing scopes for your access token). Error response included.
# 404 Not Found Request failed, due to the resource not being found. Error response included.
# 405 Method Not Allowed Request failed, due to unsupported HTTP method. Error response included.
# 409 Conflict Request failed, due to the current state of the resource (e.g. edit a deopsition which is not fully integrated). Error response included.
# 415 Unsupported Media Type Request failed, due to missing or invalid request header Content-Type. Error response included.
# 429 Too Many Requests Request failed, due to rate limiting. Error response included.
# 500 Internal Server Error

def sorse_zenodo_upload(args):
    # pure for convenience...
    inputpath = args.inputpath
    sandboxing = args.sandboxing
    communityid = args.communityid
    publish = args.publish
    overwrite = args.overwrite
    workingpath = args.workingpath

    access_token = args.token if not args.token is None else os.getenv('ZENODO_SANDBOX_TOKEN') if sandboxing else os.getenv('ZENODO_TOKEN')
    api_uri = 'https://sandbox.zenodo.org' if sandboxing else 'https://zenodo.org'
    headers = {"Content-Type": "application/json"}
    params = {'access_token': access_token}

    # loop through inputpath
    logging.info('Searching %s for events', inputpath)
    events = Path(inputpath).rglob('*.md')
    for path in events:
        print("Processing {}".format(path))
        logging.info("Processing %s", path)
        post = frontmatter.load(path)
        if 'publish' in post and post['publish'] == 'no':
            logging.info("Found 'publish': 'no' field. Skipping %s", path)
            continue
        if not 'title' in post or not 'affiliations' in post:
            logging.error('Could not find a title or affiliations in the frontmatter in event %s, check file contents.', path)
            print("Error processing {}, check log file for more information".format(path))
            continue
        logging.info("Found event %s (%s)", post['title'], path)
        if 'doi' in post:
            logging.info("Event already deposited! Check DOI %s. Skipping...", post['doi'])
            print("Error processing {}, check log file for more information".format(path))
            continue
        # Create empty deposition - Should return 201
        logging.info("Creating new deposition for %s", path)
        r = requests.post(api_uri+'/api/deposit/depositions',
            params=params,
            json={},
            headers=headers)
        
        if (r.status_code != 201):
            logging.error("Failed to create empty deposition! Response: %i: %s", r.status_code, r.content)
            print("Error processing {}, check log file for more information".format(path))
            continue
        # Fetch DOI from prereservation
        doi = r.json()['metadata']['prereserve_doi']['doi']
        # Fetch bucket url to put files
        bucket_url = r.json()["links"]["bucket"]
        # Fetch deposition id for next requests
        deposition_id = r.json()['id']
        logging.info("Received info for new deposition: id: %s, doi: %s, bucket_url: %s", deposition_id, doi, bucket_url)
        # Fetch authors from frontmatter and resolve affiliations links
        authors = post['authors']
        affiliations = post['affiliations']
        creators = []
        for aut in authors:
            creator = dict()
            creator['name'] = aut['name']
            if not 'affiliation' in aut:
                logging.error('Author %s in event %s does not have an affiliation! Defaulting to N/A', aut['name'], path)
                creator['affiliation'] = 'N/A'
            else:
                aff_index = aut['affiliation']
                # find affiliation string
                for keyval in affiliations:
                    if aff_index == keyval['index']:
                        creator['affiliation'] = keyval['name']
                        break
            if 'orcid' in aut:
                creator['orcid'] = aut['orcid'] 
            
            # do not add other author fields, because the Zenodo API will complain
            creators.append(creator)
        
        # update .md with DOI
        post['doi'] = doi
        filename, file_extension = os.path.splitext(str(path))
        outputpath = str(path) if overwrite else filename+'-new'+file_extension
        output_file = open(outputpath, 'wb')
        frontmatter.dump(post, output_file)
        output_file.close()
        # generate PDF
        temp_file = open(workingpath + '/' + path.name, 'wb')
        frontmatter.dump(post, temp_file)
        temp_file.close()
        # copyfile(outputpath, './generate-pdf/'+ path.name) # this might not finish before the subprocess call
        subprocess.call(['sh', './generate-pdfs.sh'])
        # os.remove('./generate-pdf/'+ path.name)

        # The target URL is a combination of the bucket link with the desired filename
        # seperated by a slash.
        pdfpath = workingpath + '/' + os.path.basename(filename) + '.pdf' # use the event filename for the pdf
        logging.info("Uploading file contents for %s", pdfpath)
        
        with open(pdfpath, "rb") as fp:
            r = requests.put(
                "%s/%s" % (bucket_url, os.path.basename(filename) + '.pdf'),
                data=fp,
                params=params,
            )
        if (r.status_code != 200):
            logging.error("Failed upload file contents! Response: %i: %s", r.status_code, r.content)
            print("Error processing {}, check log file for more information".format(path))
            continue
        logging.info("File contents uploaded for %s", pdfpath)
    
        # add metadata to deposition
        data = { 'metadata': {
            'publication_date': str(post['date']),
            'title': post['title'],
            'upload_type': 'publication',
            'publication_type': 'conferencepaper',
            'description': post.content,
            'creators': creators,
            'communities': [{'identifier': communityid}],
            'conference_title': 'International Series of Online Research Software Events',
            'conference_acronym': 'SORSE', 
            'conference_url': 'https://sorse.github.io',
            'access_right': 'open',
            'license': 'cc-by-4.0'
            },    
        }
        logging.info("Constructed metadata for {}: {}".format(path, data))
        
        r = requests.put(api_uri+'/api/deposit/depositions/%s' % deposition_id, 
                    params=params, data=json.dumps(data),
                    headers=headers)
        if (r.status_code != 200):
            logging.error("Failed to add metadata to deposition! Response: %i: %s", r.status_code, r.content)
            print("Error processing {}, check log file for more information".format(path))
            continue
        logging.info("Metadata added for %s", path)
        
        if publish:
            # publish deposition
            logging.info("Publishing content for event %s", path)
            r = requests.post(api_uri+'/api/deposit/depositions/%s/actions/publish' % deposition_id,
                       params=params)
            if (r.status_code != 202):
                logging.error("Failed to publish deposition! Response: %i: %s", r.status_code, r.content)
                print("Error processing {}, check log file for more information".format(path))
                continue
            logging.info("Deposition published for %s", path)
        logging.info("Finished processing %s", path)

if __name__ == "__main__":
    load_dotenv() # for Zenodo Token
    parser = ArgumentParser("SORSE Zenodo Upload script. This script will browse recursively through INPUTPATH and look for .md files that match the format of the SORSE website.")
    parser.add_argument('--sandboxing', help='If supplied, Zenodo Sandbox will be used instead.', required=False, action='store_true')
    parser.add_argument('--inputpath',  help='The root folder for the input files.', required=True)
    parser.add_argument('--workingpath', help='The folder that will be used to create new markdowns and pdfs', default='../ci', required=False)
    parser.add_argument('--overwrite', help='If supplied, DOIs will be added inline to input files. Otherwise *-new.md files will be created', required=False, action='store_true')
    parser.add_argument('--token', help='If not provided in .env as ZENODO_TOKEN (or ZENODO_SANDBOX_TOKEN), you can supply the Zenodo Token here.', required=False)
    parser.add_argument('--communityid', help='Community ID to be used in Zenodo.', required=False, default='sorse')
    parser.add_argument('--publish', help='If supplied, depositions will be published as well.', required=False, action='store_true')
    
    args = parser.parse_args()
    print(args.communityid)
    logging.basicConfig(filename='sorse_zenodo_upload.log', level=logging.DEBUG)
    logging.info('*** Sorse Zenodo Upload Start ***')
    sorse_zenodo_upload(args)
    logging.info('*** Sorse Zenodo Upload Stop ***')