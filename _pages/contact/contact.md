---
permalink: /contact/
title: "Contact"
sidebar:
  nav: "contact"
author: de-RSE
---

## Who is organising SORSE?
We are an international committee of RSEs from various [national RSE chapters](chapters). Those who support RSEs, researchers and others who are enthusiastic about maintaining opportunities to learn about research software and keep the community in touch online through challenging times.

## Get in touch
This conference is organized by Research Software Engineers like you!

- If you have any questions concerning the conference, please contact the organizers of the conference via [{{ site.email }}](mailto:{{ site.config.email }})
- For any other issues with the conference website, please contact the [website chair](#international-committee-members).


## SORSE20 Organizers

<div style="display: flex; flex-wrap: wrap;">
  {% for person in site.data.committee.members %}
  {% include card.html info=person %}
  {% endfor %}
</div>
