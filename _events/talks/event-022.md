---
affiliations:
- index: 1
  name: University of Oxford, UK
author: &id001
  affiliation: 1
  email: adutta@robots.ox.ac.uk
  is_speaker: true
  name: Dr. Abhishek Dutta
  orcid: 0000-0002-5455-3343
authors:
- *id001
category: talks
date: 2020-09-09
doi: 10.5281/zenodo.4298671
language: English
last_modified_at: 2020-09-15
recording_url: https://youtu.be/WNgHy2hIuUI
registration_url: https://indico.scc.kit.edu/event/935/
slides: https://indico.scc.kit.edu/event/935/attachments/3835/5636/sorse_adutta_20-11-10.pdf
time:
- - end: 2020-11-10 11:00:00+00:00
    start: 2020-11-10 10:30:00+00:00
title: Learnings from developing and maintaining a research software that has been
  used more than 3 million times in the last 3 years
---

Manually annotated images and videos are a fundamental part of many research projects and industrial applications. However, manual image annotation tools are often designed to address one specific use case and lack the flexibility to be reused across different projects. Furthermore, these tools often have complex installation and setup procedure which presents a barrier to non-technical users. To address these limitations, we created the VGG Image Annotator [VIA](http://www.robots.ox.ac.uk/~vgg/software/via/),  which is a light weight, standalone and offline software package that does not require any installation or setup and runs solely in a web browser. The VIA software allows human annotators to define and describe spatial regions in images or video frames,  and temporal segments in audio or video. These manual annotations can be exported to plain text data formats such as JSON and CSV and therefore are amenable to further processing by other software tools. VIA also supports collaborative annotation of a large dataset by a group of human annotators. The BSD open source license of this software allows it to be used in any academic project or commercial application.

The VIA software has quickly become an essential and invaluable research support tool in many academic disciplines. Furthermore, it has also been immensely popular in several industrial sectors which have invested in adapting this open source software to their specific requirements. In this talk, we will share our learnings from developing and maintaining this open source research software that has been used more than 3,000,000 times since its public release in April 2017.