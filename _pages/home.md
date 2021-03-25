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

{% capture final-notice %}
SORSE ended with its [final event]({{ "/programme/finale/" | relative_url }})
on March 24th 2021. Thanks to all the contributors who submitted abstracts and
gave presentations, discussions, demonstrations, and thanks to everyone who
participated in one of our sessions to make all of this possible.

But this isn't the end. There is still a need for knowledge exchange and networking within our international community of Research Software Engineers.

Stay tuned and keep an eye on the communication channels of
[your national RSE chapter]({{ "/contact/chapters/" | relative_url }}).
{% endcapture %}

Welcome to SORSE - A **S**eries of **O**nline **R**esearch **S**oftware **E**vents - our international answer to the COVID-19-induced cancellation of many national RSE conferences. We want to provide an opportunity for RSEs to develop and grow their skills, build new collaborations and engage with RSEs worldwide.

This series has been an open call to all RSEs and anyone involved with research software worldwide, to propose a talk, a workshop, a software demo, a panel or discussion, blog post or poster. After each event, SORSE did provide an opportunity for networking and informal discussion with other participants in small groups.

<div class="notice--info">
  {{ final-notice | markdownify }}
</div>

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
