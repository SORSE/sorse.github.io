---
title: "Lightning talk session"
category: news
permalink: /programme/posters/session/
tags:
  - announcement
  - contribution
  - posters
sidebar:
  nav: programme
classes: wide
id: 1
include_in_calendar: true
last_modified_at: 2021-01-15
registration_url: https://indico.scc.kit.edu/event/2295/
time:
  - - start: 2021-01-20T15:00:00Z
      end: 2021-01-20T16:00:00Z
---

We will run a lightning talk session on Wed 20th January 2021 at 3pm UTC.

<div>
    {% assign time = page.time[0][0] %}
    {% include registration-button.html %}
    {% include add-to-calendar-button.html %}
</div>

Lightning talks of up to 5 minutes will be presented at the start of the session. Each presenter will then be available in a break out room with video and text chat facilities to discuss their poster or blog post with those attending. Attendees can move between break out rooms to discuss different posters and blog posts. Posters and blog posts will be available a few days in advance of the session to allow attendees to read the material beforehand.

## Lightning talks

We are pleased to be welcoming the following lightning talks:

{%- assign posts = site.events | where: "category", "posters" -%}
{%- for post in posts -%}
{%- if post.time and post.time[0][0].start == page.time[0][0].start -%}
{% include event-card.html %}
{%- endif -%}
{%- endfor -%}
