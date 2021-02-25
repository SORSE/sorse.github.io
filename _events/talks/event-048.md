---
affiliations:
- index: 1
  name: Alfred-Wegener-Institut Helmholtz-Zentrum für Polar- und Meeresforschung (AWI),
    Germany
- index: 2
  name: GEOMAR Helmholtz Centre for Ocean Research Kiel, Germany
- index: 3
  name: German Research Centre for Geosciences (GFZ), Germany
- index: 4
  name: Helmholtz Zentrum Geesthacht (HZG), Institute for Coastal Research, Germany
- index: 5
  name: Helmholtz-Zentrum für Umweltforschung GmbH - UFZ, Germany
- index: 6
  name: Karlsruhe Institute of Technology, Institute of Meteorology and Climate Research
    - Atmospheric Environmental Research (IMK-IFU), Germany
author: &id001
  affiliation: 4
  email: philipp.sommer@hzg.de
  is_speaker: true
  name: Philipp S. Sommer
  orcid: 0000-0001-6171-7716
authors:
- *id001
- affiliation: 4
  name: Viktoria Wichert
  orcid: 0000-0002-3402-6562
- affiliation: 3
  name: Daniel Eggert
  orcid: 0000-0003-0251-4390
- affiliation: 1
  name: Tilman Dinter
  orcid: 0000-0002-1505-8833
- affiliation: 2
  name: Klaus Getzlaff
  orcid: 0000-0002-0347-7838
- affiliation: 2
  name: Andreas Lehmann
  orcid: 0000-0001-5618-6105
- affiliation: 6
  name: Christian Werner
  orcid: 0000-0001-7032-8683
- affiliation: 1
  name: Brenner Silva
- affiliation: 5
  name: Lennart Schmidt
- affiliation: 1
  name: Angela Schäfer
  orcid: 0000-0003-1784-2979
category: talks
date: 2021-02-19
doi: 10.5281/zenodo.4551996
language: English
last_modified_at: 2021-02-19
prerequisites: A bit of background in Python would be helpful but not mandatory
time:
- - end: 2021-03-03 10:45:00+00:00
    start: 2021-03-03 10:30:00+00:00
title: A new distributed data analysis framework for better scientific collaborations
registration_url: https://indico.scc.kit.edu/event/2327/
---

A common challenge for projects with multiple involved research institutes is a well-defined and productive collaboration. All parties measure and analyze different aspects, depend on each other, share common methods, and exchange the latest results, findings, and data. Today this exchange is often impeded by a lack of ready access to shared computing and storage resources. In our talk, we present a new and innovative remote procedure call (RPC) framework. We focus on a distributed setup, where project partners do not necessarily work at the same institute, and do not have access to each others resources.
We present an application programming interface (API) developed in Python that enables scientists to collaboratively explore and analyze sets of distributed data. It offers the functionality to request remote data through a comfortable interface, and to share and invoke single computational methods or even entire analytical workflows and their results. The prototype enables researchers to make their methods accessible as a backend module running on their own infrastructure. Hence researchers from other institutes may apply the available methods through a lightweight python or Javascript API.  In the end, the overhead for both, the backend developer and the remote user, is very low. The effort of implementing the necessary workflow and API usage equalizes the writing of code in a non-distributed setup. Besides that, data do not have to be downloaded locally, the analysis can be executed "close to the data" while using the institutional infrastructure where the eligible data set is stored.
With our prototype, we demonstrate distributed data access and analysis workflows across institutional borders to enable effective scientific collaboration.
This framework has been developed in a joint effort of the DataHub and Digitial Earth initiatives within the Research Centers of the Helmholtz Association of German Research Centres, HGF.
