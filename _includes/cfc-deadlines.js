{%- for deadline in site.data.cfc_deadlines -%}
{%- capture deadline_start -%}{{ deadline }}T23:00:00-0100{%- endcapture -%}
{%- capture deadline_end -%}{{ deadline }}T23:00:00-0100{%- endcapture -%}
{
  title  : 'Submission deadline',
  url    : "{{ '/programme/call-for-contributions/' | relative_url }}",
  display: "block",
  color  : "#d8b117",
  textColor: "#740B70",
  classNames: ["fg-cfc-deadline"],  // to change the font-weight
  start  : "{{ deadline_start | date_to_xmlschema }}",
  end    : "{{ deadline_end | date_to_xmlschema }}"
}{% unless forloop.last %},{% endunless %}
{%- endfor -%}
