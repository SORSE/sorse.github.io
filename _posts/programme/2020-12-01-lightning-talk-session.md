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
time:
  - - start: 2021-01-20T15:00:00Z
    - end: 2021-01-20T16:00:00Z
---

We will run a lightning talk session on Wed 20th January 2021 at 3pm UTC.  The session will be a one hour slot and include up to 10  lightning talks. Each lightning talk should be supported by either a poster or a blog post.

<p>
    {% assign time = page.time[0][0] %}
    {% include add-to-calendar-button.html %}
</p>

Presenters will be asked to pre-record a 1 to 2 minute lightning talk which will be played at the start of the session. Each presenter will then be available in a break out room with video and text chat facilities to discuss their poster or blog post with those attending. Attendees can move between break out rooms to discuss different posters and blog posts.  Posters and blog posts will be available a few days in advance of the session to allow attendees to read the material beforehand. Posters will be maximum A1 size. Blog posts should be between 700 and 2000 words.

**Deadline for submissions is midnight UTC of January 10th, 2021.**

## Brief summary

* up to 10 lightning talks on 20th January 2021 at 3pm UTC
* posters max A1 size
* blog post 700-2000 words
* lightning talk session - pre-record talk 1-2 minutes
* followed by breakout session

## Lightning talks

{%- assign posts = site.events | where: "category", "posters" -%}
{%- for post in posts -%}
{% include event-card.html %}
{%- endfor -%}
