---
affiliations:
- index: 1
  name: Durham University, UK
author: &id001
  affiliation: 1
  email: tobias.weinzierl@durham.ac.uk
  is_speaker: true
  name: Dr. Tobias Weinzierl
  orcid: 0000-0002-6208-1841
authors:
- *id001
category: talks
date: 2020-11-03
doi: 10.5281/zenodo.4430837
language: English
last_modified_at: 2021-01-10
prerequisites: None. Interest in numerical simulations will make the talk more relevant
  to the audience.
registration_url: https://indico.scc.kit.edu/event/2260/
time:
    - - start: 2021-01-26T14:00:00Z
        end: 2021-01-26T14:30:00Z
title: My project expired and my team left, so let's rewrite all the software from
  scratch
slides: https://indico.scc.kit.edu/event/2260/contributions/7978/attachments/3862/5946/SORSE_Session_Slides_2021-01-26-2talk.pdf
recording_url: https://youtu.be/lRO0LVuBMkU
---

Peano is a framework for large-scale simulations using dynamically adaptive
Cartesian grids. It is used today for Earthquake and Black Hole simulations,
for example. The fourth generation of the software is
currently under development.

Peano's development as well as the push behind ExaHyPE, a solver engine built
upon Peano, always has been shaped by the ambition to implement
state-of-the-art numerics. In our field, this implies multiscale algorithms
where others work with "flat" data structures, dynamically changing
data structures where others rely on something static, writing
multi-numerics/multi-physics codes where others focus on one thing, supporting hybrid architectures where others commit either to GPGPU- or
CPU-only, and so forth.

In this talk I briefly categorise the software and present application areas. After that, I focus on the software's genesis. Peano
has started off as a collection of codes for solving incompressible fluids,
yet spread out into many application areas,
it has been shaped (and misshaped) by dozens of core
developers, and it has grown repeatedly into a state that
made it hard to maintain and extend further. Therefore, each generation has
become a complete rewrite---also as we tried to bring in new, fancy numerics
every time.

I will explain which software design patterns we use today in our framework
in an attempt to deliver software that is fast, maintainable and usable for
all the different communities involved. With our complex agenda, it is basically
impossible to find developers among PhDs, academics or RSEs that master all
areas of relevance. So we need a strict separation of concerns (and flaws)
which materialises in our code as the Hollywood Principle: Don't call us, we
call you. In short, we take a lot of freedom away from developers how they
can realise things. Instead, we force them to focus on what they want to do.