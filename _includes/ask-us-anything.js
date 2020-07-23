{% for time in site.data.ask_us_anything %}
{
  title: "Ask us anything",
  {%- if include.onclick == 'tag' %}
  url: "#ask-us-anything-sessions",
  {%- else %}
  url: "{{ '/programme/ask-us-anything/' | relative_url }}",
  {%- endif %}
  display: "block",
  color: "#A05F9D",
  start: '{{ time }}',
  end: new Date('{{ time }}') + (60 * 60 * 1000)
}{% unless forloop.last %},{% endunless %}
{% endfor %}
