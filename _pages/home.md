---
permalink: /
title: "SORSE - International Series of Online Research Software Events"
sidebar:
  nav: "news"
author: SORSE
author_profile: false
---

<a href="{{site.indico_base_event}}/abstracts" class="btn btn--success" target="_blank"><i class="fas fa-pen"></i> Submit an abstract</a>

Welcome to SORSE - A **S**eries of **O**nline **R**esearch **S**oftware **E**vents - our international answer to the COVID-19-induced cancellation of many national RSE conferences. We want to provide an opportunity for RSEs to develop and grow their skills, build new collaborations and engage with RSEs worldwide. This is an open call to all RSEs and anyone involved with research software, worldwide, to propose talks, workshops and other types of online events.

Any questions, read [more](faq/about/what-is-sorse) or [get in touch](contact/)!

### News

{% if paginator %}
  {% assign posts = paginator.categories["news"] %}
{% else %}
  {% assign posts = site.categories["news"] %}
{% endif %}

{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}

{% include paginator.html %}
