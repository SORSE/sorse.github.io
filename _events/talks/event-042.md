---
affiliations:
- index: 1
  name: Deutsches Archäologisches Institut, Germany
- index: 2
  name: Römisch-Germanisches Zentralmuseum, Germany
- index: 3
  name: Verbundzentrale des GBV, Germany
author: &id001
  affiliation: 2
  is_speaker: true
  name: Florian Thiery
  orcid: 0000-0002-3246-3531
authors:
- *id001
- affiliation: 1
  is_speaker: true
  name: Sophie Charlotte Schmidt
  orcid: 0000-0003-4696-2101
- affiliation: 3
  name: Jakob Voß
  orcid: 0000-0002-7613-4123
category: talks
date: 2021-02-19
doi: 10.5281/zenodo.4551994
language: English
last_modified_at: '2021-02-19'
prerequisites: (semantic) data modelling, data publishing
time:
- - end: 2021-03-03 10:30:00+00:00
    start: 2021-03-03 10:00:00+00:00
title: Wikidata as a research tool for data modelling and integration in the humanities
  - Examples from the German Wikimedia Fellow Program Free Knowledge
---

Research Software Engineers and their work is becoming increasingly important in digital humanities research just as digital humanities gain traction. Not just developing and extending software are important for this process, data creation, data publication and data management are equally critical; as the idiom goes, "data matures like wine, applications like fish". Therefore, RSEs need to store their 'wine' FAIRly to make it accessible in the future. In this talk we present Wikidata as a data integration hub for FAIR Linked Open Data (LOD), that can be used with many research software tools, e.g. SPARQLing Unicorn, QGIS plugin and Scholia. Wikidata is the information storage system in the Wikimedia Universe. In particular, Wikidata is ideal for data modeling and immediate publishing as any user can create their own (semantic) data model and map it to Wikidata. A number of tools and APIs already exist for applying Wikidata to open research [1]. As an example use case we will present two projects from the German Wikimedia Fellow-Programme Free Knowledge. The first, Irish Ogham Stones in the Wikimedia Universe [2], focuses on linking different data sets on Ogham Stones within the Wikimedia Universe and the second, Smashed Dishes -- Archaeological Sources in Wikidata [3], aims to create possibilities for amateur archaeologists to collect and publish their data. As a conclusion, we will discuss the advantages we found in using Wikidata. These include enhanced data re-usability and availability, FAIRly published data and data and possibilities for data integration between diverse data sources and research software. Data and software integration may lead to Linked Open Data and, the resulting interoperability opens up new possibilities for RSEs.

[1] https://www.wikidata.org/wiki/Wikidata:Tools/For_programmers
[2] http://ogham.squirrel.link
[3] http://smasheddishes.squirrel.link