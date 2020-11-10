---
title: "Configuring Sphinx from scratch: making your own documentation and making your documentation your own"
authors:
    - &speaker
      name:  Sadie Bartholomew
      email: sadie.bartholomew@ncas.ac.uk
      orcid: 0000-0002-6180-3603
      is_speaker: true
      affiliation: 1
affiliations:
    - name: National Centre for Atmospheric Science, UK
      index: 1
time: 
    - - start: 2020-11-03T15:00:00Z
        end: 2020-11-03T16:00:00Z
author: *speaker
category: software-demos
language: English
doi: 10.5281/zenodo.3977886
prerequisites: "Basic familiarity with Python and the command line"
license: Open source
date: 2020-07-17
last_modified_at: 2020-11-10
instructions: "<a href='https://www.sphinx-doc.org/en/master/usage/installation.html#installation-from-pypi' class='truncated'>https://www.sphinx-doc.org/en/master/usage/installation.html#installation-from-pypi</a>"
registration_url: https://indico.scc.kit.edu/event/918/
slides: https://github.com/sadielbartholomew/sphinx-from-scratch
recording_url: https://youtu.be/Xjei353h-f0
---
In this demonstration we will build a mature documentation system from scratch for a dummy project using the Sphinx documentation generator, the infrastructure of choice for the documentation of a huge number of modern software projects, including of Python itself.

We begin with the basics: writing reStructuredText content and configuring a build to convert it into the desired output(s), taking HTML and LaTeX outputs as an example. We then cover just some of the many ways you can customise the structure, style and capability of your Sphinx project to 'make it your own', so it fits with the specific needs of your audience. Whether you want to setup dedicated documentation for a project, or want a home for notes on a topic, or even a book, we aim to showcase that a Sphinx project can be an easy, flexible and powerful means to store and develop your content.

This demonstration requires some familiarity with Python and the Linux shell (command line).
