---
title: "Towards Knowledge Graphs of Research Software metadata"
authors:
    - &speaker
      name:  Daniel Garijo
      email: dgarijo@isi.edu
      orcid: 0000-0003-0454-7145
      is_speaker: true
      affiliation: 1
    - name:  Yolanda Gil
      affiliation: 1
    - name: Maximiliano Osorio
      affiliation: 1
    - name:  Varun Ratnakar
      affiliation: 1
    - name:  Deborah Khider
      affiliation: 1
affiliations:
    - name: Information Sciences Institute, USC, US
      index: 1
time:
    - - start: 2020-09-22T19:30:00Z
        end: 2020-09-22T20:00:00Z
author: *speaker
category: talks
doi: 10.5281/zenodo.3977916
language: English
prerequisites: "N/A
Knowing what Zenodo and schema.org is will help, but is not a pre-requisite."
date: 2020-07-17
last_modified_at: 2020-08-26
registration_url: https://indico.scc.kit.edu/event/915/
---
Research software is a key asset for understanding, reusing and reproducing results in computational sciences. An increasing amount of software is stored in code repositories, which usually contain human readable instructions indicating how to use it and set it up. However, developers and researchers often need to spend a significant amount of time to understand how to invoke a software component, prepare data in the required format, and use it in combination with other software. In addition, this time investment makes it challenging to discover and compare software with similar functionality. In this talk I will describe our efforts to address these issues by creating and using Open Knowledge Graphs that describe research software in a machine readable manner. Our work includes: 1) an ontology that extends schema.org and codemeta, designed to describe software and the specific data formats it uses; 2) an approach to publish software metadata as an open knowledge graph, linked to other Web of Data objects; and 3) a framework for automatically extracting metadata from software repositories; and 4) a framework to curate, query, explore and compare research software metadata in a collaborative manner. The talk will illustrate our approach with real-world examples, including a domain application for inspecting and discovering hydrology, agriculture, and economic software models; and the results of our framework when enriching the research software entries in Zenodo.org.
