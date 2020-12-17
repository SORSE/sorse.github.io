---
title: "From experimental software to research infrastructure maturity"
authors:
    - &speaker
      name:  Carsten Thiel
      email: carsten.thiel@cessda.eu
      orcid: 0000-0003-0804-8992
      is_speaker: true
      affiliation: 1
affiliations:
    - name: CESSDA, Norway
      index: 1
author: *speaker
doi: 10.5281/zenodo.3977896
category: talks
language: English
time:
    - - start: 2020-12-07T14:30:00Z
        end: 2020-12-07T15:00:00Z
prerequisites: "General familiarity with issues from software development including concepts such as testing and automation as well as project management with limitations in academia are advantageous."
date: 2020-07-17
last_modified_at: 2020-11-03
registration_url: https://indico.scc.kit.edu/event/2200/
slides: https://indico.scc.kit.edu/event/2200/attachments/3888/5763/SORSE-experimental-software-infrastructure-maturity.pdf
recording_url: https://youtu.be/CUhvbAh1hmc
---
The challenges facing research software development are manifold and have long been a major topic at RSE conferences.

In the context of the covid-19 pandemic, debates about the use or rather re-use of research software for real word applications -- with life-or-death implications -- have occurred in broader contexts than RSE conferences. The discussions confirm what has long been known: sustaining software for long term use requires continued commitment and investment in quality and practices, see e.g. Report on the [Workshop on Sustainable Software Sustainability 2019 (WOSSS19)](https://doi.org/10.5281/zenodo.3922155).

With the European Commission's plan for a European Open Science Cloud (EOSC), foundations are being laid to build an ecosystem to enable digital research. One of the core requirements for offering a service in EOSC will be its technical maturity -- it must reach an 8 on the 9-step Technology Readiness Level scale, designed by NASA to assess its technology's space readiness.

In this talk I will explain what we at CESSDA, the Consortium of European Social Science Data Archives, do to ensure our technology is designed to build services that meet these maturity requirements. Starting from guidelines and agreement on best practices, automation plays an important role for quality analysis and testing and also provides evidence of this. Investing in the long term objective of sustainability for our cloud native infrastructure plays a fundamental part. At the core, we define [repeated software releases](https://docs.tech.cessda.eu/software/releases.html) -- not just one-off demonstrators -- with strict quality requirements as the fundamental deliverables that we can later turn into [mature services](https://docs.tech.cessda.eu/services/requirements.html) we can reliably provide to our users.

We will show how our model can serve as a blueprint for EOSC and for moving from experimental code to infrastructure that is mature enough to serve its purpose in times of crisis.
