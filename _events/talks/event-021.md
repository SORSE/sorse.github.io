---
title: "Goodbot, Badbot? Engineering trust into conversational interfaces"
authors:
    - &speaker
      name: Dave Horsfall
      is_speaker: true
time: 
    - - start: 2020-11-10T10:00:00Z
        end: 2020-11-10T10:30:00Z
author: *speaker
category: talks
language: English
prerequisites: "General software engineering principles"
date: 2020-09-09
last_modified_at: 2020-09-15
registration_url: https://indico.scc.kit.edu/event/935/
slides: https://indico.scc.kit.edu/event/935/attachments/3835/5635/sorse_dhorsfall_20-11-10.pdf
---
As more people interact with bots driven by Artificial Intelligence, it is important to understand how to create relationships based on trust. The [FinTrust Project][1] at Newcastle University is looking at the role of machine learning in banking, particularly in the context of automated chatbots and how the presence of socio-emotional features impacts the intention to use. Researchers from social sciences and computing are examining how trust can be measured, how trust is gained and lost, and what implications this might have on design considerations.

The team has used theories on trust in automation, emotion, and theories of computer-human interaction to categorise trustworthy traits. Engineering these social cues as features into conversational interfaces has offered an interesting start to my RSE career, and spans a variety of areas from Natural Language Processing to careful UI Design. In this talk I will firstly discuss my step from industry into the RSE profession at the end of March, just a few days after severe lockdown restrictions where imposed by the UK government. The challenges of starting this new role and collaborating with colleagues I have been unable to meet in person have been significant, but ultimately very rewarding. I will explain my approach within this multi-disciplinary project to use [Dialogflow][2] to quickly leverage Google's powerful machine learning. This allowed us to build an operational chatbot prototype that was capable of exhibiting varying degrees of social presence, such as politeness, empathy and active listening. The talk will review the infrastructure design for AI powered chatbots, and illustrate how machine learning can interpret the intent of what users are saying, to gather information and respond appropriately.

  [1]: https://www.ncl.ac.uk/press/articles/archive/2018/11/fintrust/
  [2]: https://cloud.google.com/dialogflow
