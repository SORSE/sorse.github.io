---
affiliations:
- index: 1
  name: eLife, UK
author: &id001
  affiliation: 1
  email: e.tsang@elifesciences.org
  is_speaker: true
  name: Dr. Emmy Tsang
  orcid: 0000-0002-9248-1280
authors:
- *id001
category: software-demos
date: 2020-08-18
doi: 10.5281/zenodo.4430853
instructions: N/a
language: English
last_modified_at: '2021-01-10'
license: Open source
meeting_url: https://zoom.us/j/98656860237?pwd=dVVVZUFSdXdjRTdscnU4U2drWXNsdz09
recording_url: https://youtu.be/_uRKBdEHhS0
registration_url: https://indico.scc.kit.edu/event/913/
slides:
- Part 1: https://indico.scc.kit.edu/event/913/attachments/3608/5295/go
- Part 2: https://indico.scc.kit.edu/event/913/attachments/3608/5296/go
time:
    - - start: 2020-09-09T14:00:00Z
        end: 2020-09-09T15:00:00Z
title: 'Executable Research Article (ERA): Enrich a research paper with code and data'
---

Code and data are important research output and integral to a full understanding of research findings and experimental approaches in a paper. However, traditional research articles seldom have these embedded in the manuscript's narrative, but instead, leave them as "supplementary materials", if they are openly available.

With Executable Research Articles (ERAs, previously known as the Reproducible Document Stack (RDS)), our vision is to enrich the traditional narrative of a research article with code, data and interactive figures that can be executed in the browser, downloaded and explored. It will give readers a direct insight into the methods, algorithms and key data behind the published research.

We published our [first demo ERA][1] in February 2019. Over the past year, we have been working closely with our collaborator Stencila to build an open tool stack that would enable our authors and production team to easily publish ERAs at scale. In this talk, we hope to showcase the potential of ERAs with examples and walk through how authors can enrich their traditional eLife paper using Stencila Hub, through:

 - Starting a Stencila Hub project linked to their eLife paper
 - Converting the article to a reproducible notebook format of their
   preference, while preserving the relevant journal article metadata
 - Uploading the data required to enable live re-execution of tables and
   figures in the article
 - Replacing static tables and figures with code chunks that reproduce them

We will share our current vision of how ERAs will be integrated into our production workflow and collect feedback. We also hope to engage participants in exploring potential functionalities for the tool stack and building a community-driven roadmap.

  [1]: https://elifesciences.org/articles/30274/executable