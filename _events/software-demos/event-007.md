---
affiliations:
- index: 1
  name: King's College London, UK
author: &id001
  email: stefania.marcotti@kcl.ac.uk
  is_speaker: true
  name: Stefania Marcotti
  orcid: 0000-0002-2877-0133
authors:
- *id001
- affiliation: 1
  name: Dr. Burki Mubarik
- affiliation: 1
  name: Prof. Brian M Stramer
category: software-demos
date: 2020-11-30
doi: 10.5281/zenodo.4430857
instructions: <a href='https://github.com/stemarcotti/PIV ' class='truncated'>https://github.com/stemarcotti/PIV
  </a>the software is written in MATLAB and requires the Curve Fitting Toolbox. Unfortunately,
  MATLAB requires a personal or institutional license.
language: English
last_modified_at: 2021-01-10
license: Open source
prerequisites: no prerequisites necessary, the presentation will go through some basic
  theory at the beginning
registration_url: https://indico.scc.kit.edu/event/2262/
time:
    - - start: 2021-02-11T16:15:00Z
        end: 2021-02-11T16:45:00Z
title: Particle image velocimetry to study cell migration
recording_url: https://youtu.be/SwHozdoo7Sw
---

Particle image velocimetry (PIV) is a widely used optical method originally developed to understand fluid dynamics by tracking seeded particles moving through a fluid. In the context of biological disciplines, image-based pseudo-PIV is now a common tool to examine flows in tissues and cells, by exploiting the ability of tracking movement in time-lapse bioimages where features of interest are fluorescently tagged. A feature within a field of view at a specific time frame is searched for in subsequent frames by means of image cross-correlation. This allows for particle tracking and for the definition of a vector velocity field. We applied this technique to study cell migration, with a specific focus on retrograde flows of the actin cytoskeleton and their correlation to cell motion (Yolland et al., 2019). The aim of this software demonstration is to briefly introduce how the algorithm works, show the best strategies for parameter setting and demonstrate how to run it. Some application examples will be presented within the cell migration remit. The software can be found at [https://github.com/stemarcotti/PIV](https://github.com/stemarcotti/PIV); it is written in MATLAB and was tested with version R2018b (Curve Fitting Toolbox required).
