---
affiliations:
- index: 1
  name: Austrian Centre of Industrial Biotechnology, Austria
- index: 2
  name: Charité Berlin, Germany
- index: 3
  name: EMBL Heidelberg, Germany
author: &id001
  affiliation: 3
  email: gregor.moenke@embl.de
  is_speaker: true
  name: Dr. Gregor Mönke
authors:
- *id001
- affiliation: 1
  name: Frieda Sorgenfrei
- affiliation: 2
  name: Dr. Christoph Schmal
- affiliation: 2
  name: Dr. Adrian Granada
category: software-demos
date: 2020-09-09
doi: 10.5281/zenodo.4430851
instructions: conda config --add channels conda-forge conda install pyboat
language: English
last_modified_at: 2021-01-10
license: Open source
prerequisites: None (it's an UI)
registration_url: https://indico.scc.kit.edu/event/933/
slides: https://indico.scc.kit.edu/event/933/attachments/3900/5756/pyBOAT_SORSE.pdf
time:
    - - start: 2020-12-04T14:00:00Z
        end: 2020-12-04T15:00:00Z
title: Optimal time frequency analysis for biological data - pyBOAT
---

Methods for the quantification of rhythmic biological signals have been essential for the discovery of function and design of biological oscillators. Advances in live measurements have allowed recordings of unprecedented resolution revealing a new world of complex heterogeneous oscillations with multiple noisy non-stationary features. However, our understand- ing of the underlying mechanisms regulating these oscillations has been lagging behind, partially due to the lack of simple tools to reliably quantify these complex non-stationary features. With this challenge in mind, we have developed pyBOAT, a Python-based fully automatic stand-alone software that integrates multiple steps of non-stationary oscillatory time series analysis into an easy-to-use graphical user interface. pyBOAT implements continuous wavelet analysis which is specifically designed to reveal time-dependent features. In this work we illustrate the advantages of our tool by analyzing complex non-stationary time-series profiles. Our approach integrates data-visualization, optimized sinc-filter detrending, amplitude envelope removal and a subsequent continuous-wavelet based time- frequency analysis. Finally, using analytical considerations and numerical simulations we discuss unexpected pitfalls in commonly used smoothing and detrending operations.