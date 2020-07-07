---
title: Who is organizing SORSE
permalink: /faq/about/organizers
classes: wide
tags:
  - About
---
SORSE is organized by [volunteers]({% include fix-link.html link="/contact/" %})
from the international Research Software Engineers community. This work is made
possible by various [national RSE chapters]({% include fix-link.html link="/contact/chapters" %}),
namely

<ul>
  {% for item in site.data.committee.national_chapters %}
  {% assign org = item[1] %}
  <li>
    {{ org.long_name }}
    {% if org.website %}
    <a href="{{ org.website }}"><span><i class="elastic-fai fas fa-globe"></i></span></a>
    {% endif %}
    {% if org.email %}
    <a href="mailto:{{ org.email }}" title="{{ org.email }}"><span><i class="elastic-fai fas fa-envelope"></i></span></a>
    {% endif %}
  </li>
  {% endfor %}
</ul>

Please see the [contact page]({% include fix-link.html link="/contact/" %}) for
more information.

## Further links
{% include team-button.html team="operating" %}
