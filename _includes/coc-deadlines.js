{%- for deadline in site.data.coc_deadlines -%}
{%- capture deadline_start -%}{{ deadline }}T23:59:58Z{%- endcapture -%}
{%- capture deadline_end -%}{{ deadline }}T23:59:59Z{%- endcapture -%}
{
  title  : 'Submission deadline',
  url    : "{{ '/programme/call-for-contributions/' | relative_url }}",
  {% if include.background %}
  allDay: true,
  display: "background",
  backgroundColor  : "rgba(216, 177, 23, 0.3)",
  {% else %}
  color  : "#d8b117",
  {% endif %}
  start  : "{{ deadline_start | date_to_xmlschema }}",
  end    : "{{ deadline_end | date_to_xmlschema }}"
}{% unless forloop.last %},{% endunless %}
{%- endfor -%}
