{
  title  : '{{ post.title }}',
  url    : "{{ post.url | relative_url }}",
  allDay : {% if post.all_day %}true{% else %}false{% endif %},
  category : "{{ post.category }}",
  {% unless post.end_date %}// {% endunless %}end    : '{{ event.end_date | date_to_xmlschema }},'
  start  : '{{ post.date | date_to_xmlschema }}'
}
