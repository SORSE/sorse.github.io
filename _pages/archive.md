---
title: Posts Archive
permalink: /archive/
---

{% for post in site.posts %}{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}
{% assign yearDate = post.date | date: "%Y" %}
{% if yearDate != myDate %}{% if added %}</ul>{% endif %}
<h1 style="margin-top:20px; margin-bottom:10px">{{ yearDate }}</h1>
<ul>{% assign myDate = yearDate %}{% endif %}
   <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a> {% assign added = true %}</li>
 {% if forloop.last %}</ul>{% endif %}{% endfor %}
