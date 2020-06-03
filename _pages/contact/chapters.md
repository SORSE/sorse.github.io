---
permalink: /contact/chapters/
title: "National RSE Chapters"
sidebar:
  nav: "contact"
author: SORSE
author_profile: false
toc: true
toc_sticky: true
---

Members of the following national RSE Chapters are involved in the organization
of this online event.

<div style="display: flex; flex-wrap: wrap;">
{% for item in site.data.committee.national_chapters %}
{% assign chapter = item[1] %}
{% include card.html info=chapter %}
{% endfor %}
</div>

Any questions, please [get in touch](..)!


{% for item in site.data.committee.national_chapters %}
{% assign org = item[0] %}
{% assign info = item[1] %}
<h2 id="{{ org }}">{{ info.name }} {% if info.website %}<a href="{{ info.website }}"><span><i class="fas fa-globe"></i></span></a>{% endif %}</h2>
{% include team-members.html team=org %}

{% endfor %}
