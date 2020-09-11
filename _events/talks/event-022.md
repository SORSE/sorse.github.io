---
title: "Learnings from developing and maintaining a research software that has been used more than 3 million times in the last 3 years"
authors:
    - &speaker
      name: Dr. Abhishek Dutta
      email: adutta@robots.ox.ac.uk
      orcid: 0000-0002-5455-3343
      is_speaker: true
      affiliation: 1
affiliations:
    - name: University of Oxford, UK
      index: 1
author: *speaker
category: talks
language: English
date: 2020-09-09
---
Manually annotated images and videos are a fundamental part of many research projects and industrial applications. However, manual image annotation tools are often designed to address one specific use case and lack the flexibility to be reused across different projects. Furthermore, these tools often have complex installation and setup procedure which presents a barrier to non-technical users. To address these limitations, we created the VGG Image Annotator [VIA](http://www.robots.ox.ac.uk/~vgg/software/via/),  which is a light weight, standalone and offline software package that does not require any installation or setup and runs solely in a web browser. The VIA software allows human annotators to define and describe spatial regions in images or video frames,  and temporal segments in audio or video. These manual annotations can be exported to plain text data formats such as JSON and CSV and therefore are amenable to further processing by other software tools. VIA also supports collaborative annotation of a large dataset by a group of human annotators. The BSD open source license of this software allows it to be used in any academic project or commercial application.

The VIA software has quickly become an essential and invaluable research support tool in many academic disciplines. Furthermore, it has also been immensely popular in several industrial sectors which have invested in adapting this open source software to their specific requirements. In this talk, we will share our learnings from developing and maintaining this open source research software that has been used more than 3,000,000 times since its public release in April 2017.
