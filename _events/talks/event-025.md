---
affiliations:
- index: 1
  name: Harvard University, Faculty of Arts and Sciences Research Computing (FASRC),
    US
author: &id001
  affiliation: 1
  email: sarahleinicke@g.harvard.edu
  is_speaker: true
  name: Sarah Leinicke
authors:
- *id001
- affiliation: 1
  name: Mahmood Shad
category: talks
date: 2020-09-09
doi: 10.5281/zenodo.4298673
language: English
prerequisites: All experience levels are welcome.
title: Development of an Automated High-Throughput Animal Training Platform
---

In traditional neuroscience laboratory research, training animals to execute sensorimotor tasks is time consuming, labor and resource intensive, and prone to human bias and error.  The Research Software Engineering team at Harvard University's Faculty of Arts and Science Research Computing (FASRC) has developed an automated training system pipeline that standardizes and automates animal training.  The pipeline consists of Teensy microcontrollers that monitor animal training events, RaspberryPis that orchestrate and log training instructions, PiCameras that record subjects, and open-source software, including a Vue web interface, a Flask server, and a PostGreSQL database.

The automated training system produces comparable learning rates to the traditional neuroscience model, with a fraction of the effort and at minimal cost.  In this lightening talk, we will review the hardware and software pipelines and describe how researchers use the tool.