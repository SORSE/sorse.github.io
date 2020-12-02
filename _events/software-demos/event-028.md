---
title: "European Environment for Scientific Software Installations (EESSI)"
authors:
    - &speaker
      name: Kenneth Hoste
      email: kenneth.hoste@ugent.be
      is_speaker: true
      affiliation: 1
affiliations:
    - name: Ghent University, Belgium
      index: 1
time:
    - - start: 2020-11-25T15:00:00Z
        end: 2020-11-25T16:00:00Z
author: *speaker
category: software-demos
language: English
prerequisites: "- basic experience with installing/using scientific software in a Linux or macOS environment
- basic knowledge of using a Linux shell environment"
license: Open source
instructions: "<a href='https://eessi.github.io/docs/pilot' class='truncated'>https://eessi.github.io/docs/pilot</a>"
date: 2020-11-03
registration_url: https://indico.scc.kit.edu/event/2201/
slides: https://indico.scc.kit.edu/event/2201/attachments/3859/5686/EESSI-SORSE-20201125.pdf
recording_url: https://youtu.be/aEBYo7KrcN4
---
What if there was a way to avoid having to install a broad range of scientific software from scratch on every workstation, HPC cluster, or cloud instance you use or maintain, without compromising on performance?

![EESSI]({{ "/assets/images/EESSI_logo_horizontal.png" | relative_url }})

The **European Environment for Scientific Software Installations** (EESSI, pronounced as "easy") is a brand new collaboration between different European HPC sites & industry partners, with the common goal to set up a shared repository of scientific software installations that can be used on a variety of systems, regardless of the OS or processor architecture of the client system, or whether it's a full size HPC cluster, a cloud environment or a personal workstation.

The concept is heavily inspired by the [Compute Canada software stack](https://dl.acm.org/doi/10.1145/3332186.3332210), and consists of 3 layers:

* a distributed filesystem layer leveraging the established [CernVM-FS](https://cernvm.cern.ch/portal/filesystem) technology;
* a compatibility layer using [Gentoo Prefix](https://wiki.gentoo.org/wiki/Project:Prefix) to install a limited set of "system" packages;
* a software layer hosting scientific software installations and the required dependencies, which were built for different processor architectures, and where [archspec](https://github.com/archspec/archspec), [EasyBuild](https://easybuilders.github.io/easybuild) and [Lmod](https://github.com/TACC/Lmod) are leveraged;

We will present how the EESSI project grew out of a need for more collaboration to tackle the challenges in the changing landscape of scientific software and HPC system architectures. The project structure will be explained in more detail, covering the motivation for the layered approach and the choice of tools, as well as the lessons learned from the work done by Compute Canada. The goals we have in mind and how we plan to achieve them going forward will be outlined.

Finally, we will demonstrate the current pilot version of the project, and give you a feeling of the potential impact.

For more information about the EESSI project:

* website: [https://www.eessi-hpc.org](https://www.eessi-hpc.org)
* GitHub: [https://github.com/EESSI](https://github.com/EESSI)
* documentation: [https://eessi.github.io/docs](https://eessi.github.io/docs)
* Twitter: [https://twitter.com/eessi_hpc](https://twitter.com/eessi_hpc)
