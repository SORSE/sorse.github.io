---
affiliations:
- index: 1
  name: Teri Apps
author: &id001
  affiliation: 1
  is_speaker: true
  name: Teri Forey
authors:
- *id001
category: posters
date: 2021-01-13
doi: 10.5281/zenodo.4439264
language: English
last_modified_at: '2021-01-14'
prerequisites: Knowledge of APIs and web development practises would be helpful but
  not necessary.
title: Embedding a Jupyter Notebook
time:
  - - start: 2021-01-20T15:00:00Z
    - end: 2021-01-20T16:00:00Z
---

Many RSEs and researchers are familiar with using Jupyter Notebooks to analyse data and output results, but how can this functionality be included within a larger platform or application? Creating a new analysis tool would take a lot of developer hours, and so a more cost-effective solution could be to embed Jupyter within your application.

This is the approach I took last year and in this lightning talk and blog post I will describe how it works, and what were the major hurdles to overcome. I will show you how to connect Jupyter to your authentication system, integrate it with your UI and how to avoid setting up a file system.

This lightning talk should be accessible to all RSEs but will be of particular interest to those developing web applications and analysis platforms.

The blog post that accompanies the lightning talk has already been published on Medium, but I would like this opportunity to share the information with a wider audience.