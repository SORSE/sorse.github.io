---
affiliations:
- index: 1
  name: Harvard University, US
author: &id001
  affiliation: 1
  is_speaker: true
  name: Dr. Ana Trisovic
authors:
- *id001
- affiliation: 1
  name: Dr. Merce Crosas
category: talks
date: 2020-08-18
doi: 10.5072/zenodo.703754
language: english
last_modified_at: 2020-08-26
recording_url: https://youtu.be/OEY74uj8VyY
registration_url: https://indico.scc.kit.edu/event/916/
slides: https://indico.scc.kit.edu/event/916/attachments/3825/5615/Improving_FAIRness_with_containers.pdf
time:
- - end: 2020-10-07 16:30:00+00:00
    start: 2020-10-07 16:00:00+00:00
title: Improving FAIRness with containers
---

The FAIR guiding principles state that published research objects should be made Findable, Accessible, Interoperable, and Reusable for other researchers. Data repositories provide research dissemination following FAIR principles while also developing standards and tools to facilitate them. However, increased use of advanced research methods, such as virtual containers, supercomputers and GPUs, is introducing new challenges for research sharing. There is no standardized way of describing and disseminating such research outputs in data repositories. Furthermore, dissemination of data within virtual containers like Docker may hinder some of the commonly supported principles, such as findability and accessibility.

Improvements in documenting and sharing of advanced research materials in a FAIR-compliant way has recently been natively enabled in new container-based tools. This talk will present insights from community discussions on improving FAIRness with encapsulation in the context of the Dataverse data repository platform. Dataverse has a long-term commitment to preserving research artifacts to enable research transparency, reproducibility, and reuse. We will provide a review of a number of projects based on virtual containers to determine their potentials for enabling FAIRness of published research. In particular, we will review the following projects: Open Container Initiative, Singularity, ReproZip, and SciUnit, and their efforts on documenting and describing researcher's computing environments. Some of the new concepts, such as data containers and Binder Boxes will also be considered. We evaluate each of these approaches against established FAIR principles in the context of dissemination in data repositories.