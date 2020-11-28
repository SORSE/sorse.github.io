# sorse-zenodo-upload

### Assumptions
- If you do not supply a `token` with `--token <TOKEN>`, the script takes enviroment variable `ZENODO_API_TOKEN` or `ZENODO_SANDBOX_API_TOKEN` to connect to Zenodo or its Sandbox (if `--sandboxing` is provided).
- .md files have frontmatter corresponding to the SORSE format. Currently only basic checks are done, such as the presence of `title` and `affiliations` fields.
- If any goes wrong for a particular event item (.md file), the script stops processing this file, but continues with the next one. The process will not be backtracked and possibly a partial Zenodo deposition remains. Check the log file for more information.

### Installation

```
$ docker build -t rseng/pdf-generator https://github.com/rseng/pdf-generator.git
$ git clone https://github.com/johanphilips/sorse-zenodo-upload.git
$ cd sorse-zenodo-upload
$ pip install -r requirements.txt
```

### Usage

```sh
$ python sorse-zenodo-upload.py --help
usage: SORSE Zenodo Upload script. This script will browse recursively through DATA_PATH and look for .md files that match the format of the SORSE website.
       [-h] [--sandboxing] --inputpath INPUTPATH [--overwrite] [--token TOKEN]
       [--communityid COMMUNITYID] [--publish]

optional arguments:
  -h, --help            show this help message and exit
  --sandboxing          If supplied, Zenodo Sandbox will be used instead.
  --inputpath INPUTPATH
                        The root folder for the input files.
  --overwrite           If supplied, DOIs will be added inline to input files.
                        Otherwise *-new.md files will be created
  --token TOKEN         If not provided in .env as ZENODO_TOKEN (or
                        ZENODO_SANDBOX_TOKEN), you can supply the Zenodo Token
                        here.
  --communityid COMMUNITYID
                        Community ID to be used in Zenodo.
  --publish             If supplied, depositions will be published as well.
```

The script will create a log file `sorse-zenodo-upload.log` in the current directory

### Example

```sh
$ export ZENODO_SANDBOX_TOKEN=<TOKEN>
$ python sorse-zenodo-upload.py --sandboxing --inputpath ./events --communityid ecfunded
$ cat sorse-zenodo-upload.log
INFO:root:*** Sorse Zenodo Upload Start ***
INFO:root:Searching ./events for events
INFO:root:Found event SORSE Zenodo Upload Script (events\event-000.md)
INFO:root:Creating new deposition for events\event-000.md
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): sandbox.zenodo.org:443
DEBUG:urllib3.connectionpool:https://sandbox.zenodo.org:443 "POST /api/deposit/depositions?access_token=<TOKEN> HTTP/1.1" 201 978
INFO:root:Received info for new deposition: id: 703612, doi: 10.5072/zenodo.703612, bucket_url: https://sandbox.zenodo.org/api/files/84d379b5-494f-44ef-a5ab-bbfb187b35cc
INFO:root:Uploading file contents for ./generate-pdf/event-000.pdf
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): sandbox.zenodo.org:443
DEBUG:urllib3.connectionpool:https://sandbox.zenodo.org:443 "PUT /api/files/84d379b5-494f-44ef-a5ab-bbfb187b35cc/event-000.pdf?access_token=<TOKEN> HTTP/1.1" 200 708
INFO:root:File contents uploaded for ./generate-pdf/event-000.pdf
INFO:root:Constructed metadata for events\event-000.md: {'metadata': {'publication_date': '2020-11-11', 'title': 'SORSE Zenodo Upload Script', 'upload_type': 'publication', 'publication_type': 'conferencepaper', 'description': 'This fake document should only be used to test the SORSE Zenodo Upload script.', 'creators': [{'name': 'John Doe', 'orcid': '0000-0003-0937-7798', 'affiliation': 'National Centre for Research, UK'}, {'name': 'Dr. Jane Doe', 'affiliation': 'National Centre for Research, UK'}, {'name': 'Dr. Some One', 'affiliation': 'National Centre for Software, UK'}], 'communities': [{'identifier': 'ecfunded'}], 'conference_title': 'International Series of Online Research Software Events', 'conference_acronym': 'SORSE', 'conference_url': 'https://sorse.github.io', 'access_right': 'open', 'license': 'cc-by-4.0'}}
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): sandbox.zenodo.org:443
DEBUG:urllib3.connectionpool:https://sandbox.zenodo.org:443 "PUT /api/deposit/depositions/703612?access_token=<TOKEN> HTTP/1.1" 200 None
INFO:root:Metadata added for events\event-000.md
INFO:root:*** Sorse Zenodo Upload Stop ***
```

This run generated two new files [event-000-new.md](events/event-000-new.md) (`--overwrite` flag was not set) and [event-000.pdf](generate-pdfs/event-000.pdf) generated via generate-pdfs.sh. This event is also added to the Zenodo Sandbox but not yet published (`--publish` flag was not set). It did receive a prereserved DOI: 10.5072/zenodo.703612.
