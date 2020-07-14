{%- for deadline in site.data.coc_deadlines -%}
{%- capture deadline_start -%}{{ deadline }}T23:59:58Z{%- endcapture -%}
{%- capture deadline_end -%}{{ deadline }}T23:59:59Z{%- endcapture -%}
{
  title  : 'Submission deadline',
  url    : "{{ '/programme/call-for-contributions/' | relative_url }}",
  color  : "#d8b117",
  {% if include.background %}
  allDay: true,
  display: "background",
  {% endif %}
  start  : "{{ deadline_start | date_to_xmlschema }}",
  end    : "{{ deadline_end | date_to_xmlschema }}"
}{% unless forloop.last %},{% endunless %}
{%- endfor -%}
