---
title: Event buttons
permalink: /programme/calendar-buttons/
sidebar:
  nav:  programme
fullcalendar: true
---

{% assign events = '' | split: '' %}
{% for post in site.events %}
    {% if post.time %}
        {% assign events = events | push: post %}
    {% endif %}
{% endfor %}

{% for post in events %}
{%- assign event_id = post.id | split: '/' | last %}
## {{ event_id }}: {{ post.title }}
<div>
{% for time in post.time %}
{% include event-time.html %}
{% endfor %}
</div>
{% endfor %}
