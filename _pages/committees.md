---
permalink: /committees/
title: "SORSE20 Committees"
sidebar:
  nav: "news"
author: SORSE
author_profile: false
---

A committee is a group of individuals working on a component of SORSE20
{: .notice--info}

## Committees

{% for comm in site.data.committee.committees %}
<h2 id="{{ comm[0] }}">{{ comm[1].name }}</h2>
{% assign comm_id = comm[0] %}
{% include team-members.html team=comm_id %}

{% endfor %}

Any questions, please [get in touch](contact/)!
