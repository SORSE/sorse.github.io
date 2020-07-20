---
title: "Configuring Sphinx from scratch: making your own documentation & making your documentation your own"
authors:
    - &speaker name:  Sadie Bartholomew
      bio: National Centre for Atmospheric Science
      email: sadie.bartholomew@ncas.ac.uk
      orcid: 0000-0002-6180-3603
      is_speaker: true
author: *speaker
category: software-demos
language: English
prerequisites: "Basic familiarity with Python and the command line"
license: Open source
instructions: "<a href='https://www.sphinx-doc.org/en/master/usage/installation.html#installation-from-pypi'>https://sphinx-doc.org</a>"
date: 2020-07-17
---
In this demonstration we will build a mature documentation system from scratch for a dummy project using the Sphinx documentation generator, the infrastructure of choice for the documentation of a huge number of modern software projects, including of Python itself.

We begin with the basics: writing reStructuredText content and configuring a build to convert it into the desired output(s), taking HTML and LaTeX outputs as an example. We then cover just some of the many ways you can customise the structure, style and capability of your Sphinx project to ‘make it your own’, so it fits with the specific needs of your audience. Whether you want to setup dedicated documentation for a project, or want a home for notes on a topic, or even a book, we aim to showcase that a Sphinx project can be an easy, flexible and powerful means to store and develop your content.

This demonstration requires some familiarity with Python and the Linux shell (command line).
