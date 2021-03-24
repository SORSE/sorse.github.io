---
permalink: /
title: "SORSE"
sidebar:
  nav: "news"
author: SORSE
author_profile: false
layout: splash-single
header:
  overlay_image: /assets/images/sorse-banner.svg
  overlay_filter: 0.5
  actions:
    - label: Access event material
      url: programme/
    - label: Watch past events
      url: https://www.youtube.com/channel/UCJ1CwxvODyT-eb4K7HfelGA
excerpt: International Series of Online Research Software Events
---

<aside id="twitter-holder" class="sidebar__right sticky">
    {% include twitter.html %}
</aside>

Welcome to SORSE - A **S**eries of **O**nline **R**esearch **S**oftware **E**vents - our international answer to the COVID-19-induced cancellation of many national RSE conferences. We want to provide an opportunity for RSEs to develop and grow their skills, build new collaborations and engage with RSEs worldwide.

This series has been an open call to all RSEs and anyone involved with research software worldwide, to propose a talk, a workshop, a software demo, a panel or discussion, blog post or poster. After each event, SORSE did provide an opportunity for networking and informal discussion with other participants in small groups.

Any questions, read [more](faq/about/what-is-sorse) or [get in touch](contact/)!

## Past Events

Access abstracts, slides and videos through the [Programme]({{ "/programme/" | relative_url }}) page.


## Blog
{% assign posts = site.categories["blog"] %}

{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}



## News

{% if paginator %}
  {% assign posts = paginator.categories["news"] %}
{% else %}
  {% assign posts = site.categories["news"] %}
{% endif %}

{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}

{% include paginator.html %}
