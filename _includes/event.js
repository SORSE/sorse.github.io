{%- assign slot_name = "" -%}
{%- for slot in post.time -%}
{%- if forloop.index > 1 -%}
  {%- capture slot_name %} (slot #{{ forloop.index }}){% endcapture -%}
{%- endif -%}
{%- assign is_last = forloop.last -%}
{%- for time in slot -%}
{
  title  : "{{ post.title }}{{ slot_name }}{% unless forloop.first %} (continued){% endunless %}",
  {%- if include.onclick == 'tag' %}
  {%- if post.id %}
  url    : "#{{ post.id | split: '/' | last }}",
  {%- endif %}
  {%- else %}
  {%- if post.url %}
  url    : "{{ post.url | relative_url }}",
  {%- endif %}
  {%- endif %}
  allDay : {% if post.all_day %}true{% else %}false{% endif %},
  category : "{{ post.category }}",
  color  : "#474747",
  classNames: ["fc-sorse-event"],
  {% unless time.end %}// {% endunless %}end    : '{{ time.end | date_to_xmlschema }}',
  start  : '{{ time.start | date_to_xmlschema }}'
}{% unless forloop.last and is_last %},{% endunless %}
{%- endfor -%}
{%- endfor -%}
