{%- for item in site.data.cfc_deadlines -%}
{%- assign deadline = item[0] -%}
{%- assign attrs = item[1] -%}
{%- capture deadline_start -%}{{ deadline }}T23:00:00-0100{%- endcapture -%}
{%- capture deadline_end -%}{{ deadline }}T23:00:00-0100{%- endcapture -%}
{
  title: '{{ attrs.title | default: "Submission deadline"}}',
  {%- if attrs.url %}
  url    : "{{ attrs.url | relative_url }}",
  {%- else if include.onclick == 'tag' %}
  url    : "#submission-deadlines",
  {%- else %}
  url    : "{{ '/faq/howto/submission-deadlines' | relative_url }}",
  {%- endif %}
  display: "block",
  color  : "#d8b117",
  textColor: "#740B70",
  classNames: ["fg-cfc-deadline"],  // to change the font-weight
  start  : "{{ deadline_start | date_to_xmlschema }}",
  end    : "{{ deadline_end | date_to_xmlschema }}"
}{% unless forloop.last %},{% endunless %}
{%- endfor -%}
