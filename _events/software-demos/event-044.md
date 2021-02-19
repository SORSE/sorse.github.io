---
affiliations:
- index: 1
  name: Netherlands eScience Center, The Netherlands
author: &id001
  affiliation: 1
  is_speaker: true
  name: Faruk Diblen
authors:
- affiliation: 1
  email: c.martinez@esciencecenter.nl
  name: Carlos Martinez-Ortiz
  orcid: 0000-0001-5565-7577
- *id001
category: software-demos
date: 2021-02-19
doi: 10.5281/zenodo.4552004
instructions: Software can be run as a Github Action, requiring no installation. Alternatively,
  software can be run locally from command line, requiring a working python installation.
language: English
last_modified_at: 2021-02-19
license: Open source
prerequisites: Basic knowledge of Github is required, Basic knowledge of Python is
  a plus
title: How FAIR is your research software?
---

FAIR software is a topic of growing importance in the research software landscape. There have been efforts to describe the how the [FAIR principles apply to research software][1] and work in this direction is [still ongoing][2].

Even though the definition of the FAIR software principles is still in flux, [recommendations are available][3] to improve software in accordance to the spirit of the FAIR principles.

In this session we would like to introduce *[howfairis][4]*: a Python package to analyse software's compliance with the FAIR software recommendations.

We will describe how *howfairis* analyses your code to measure its level of compliance with the FAIR software recommendations. We will show how our Github Action can test your software automatically. We will also show how to add a badge to your GitHub repository showing to the world how FAIR your software is!

Given that the FAIR principles for software are still evolving, howfairis will also evolve to match new developments in the area. We would like new users to give us feedback and to contribute to the development of this tool!

  [1]: https://doi.org/10.3233/DS-190026
  [2]: https://www.rd-alliance.org/groups/fair-4-research-software-fair4rs-wg
  [3]: https://fair-software.eu/
  [4]: https://github.com/fair-software/howfairis/