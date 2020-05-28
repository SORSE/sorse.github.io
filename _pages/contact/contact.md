---
permalink: /contact/
title: "Contact"
sidebar:
  nav: "contact"
author: de-RSE
---
## Get in touch
This conference is organized by Research Software Engineers like you!

- If you have any questions concerning the conference, please contact the organizers of the conference via [{{ site.email }}](mailto:{{ site.config.email }})
- For any other issues with the conference website, please contact the [website chair](#international-committee-members).


## National RSE Chapters
<div style="display: flex; flex-wrap: wrap;">
{% for item in site.data.committee.national_chapters %}
{% assign chapter = item[1] %}
{% include card.html info=chapter %}
{% endfor %}
</div>

## International Committee Members

{% for item in site.data.committee.national_chapters %}
{% assign org = item[0] %}
{% assign info = item[1] %}
<h3 id="{{ org }}">{{ info.name }} {% if info.website %}<a href="{{ info.website }}"><span><i class="fas fa-globe"></i></span></a>{% endif %}</h3>
{% include team-members.html team=org %}

{% endfor %}
