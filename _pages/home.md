---
permalink: /
title: "SORSE20 - International Series of Online Research Software Events"
sidebar:
  nav: "news"
author: SORSE
author_profile: false
---

<aside id="twitter-holder" class="sidebar__right sticky">
  <div class='jekyll-twitter-plugin' align="center">
      {% twitter https://twitter.com/researchsofteng maxwidth=500 limit=3 %}
  </div>
</aside>

This document is work in progress!
{: .notice--danger}

Welcome to SORSE20 - A **S**eries of **O**nline **R**esearch **S**oftware **E**vents - our international answer to the COVID-19-induced cancellation of many national RSE conferences. We want to provide an opportunity for RSEs to develop and grow their skills, build new collaborations and engage with RSEs worldwide. This is an open call to all RSEs and anyone involved with research software, worldwide, to propose talks, workshops and other types of online events.

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
