---
title: Calendar
permalink: /programme/calendar/
sidebar:
  nav:  programme
classes: wide
toc: true
toc_sticky: true
fullcalendar: true
---

<div id='calendar'></div>

<script>

 document.addEventListener('DOMContentLoaded', function() {
   var calendarEl = document.getElementById('calendar');

   var calendar = new FullCalendar.Calendar(calendarEl, {
     headerToolbar: {
       left: 'prev,next today',
       center: 'title',
       right: 'dayGridMonth,listWeek,listDay'
     },
     buttonText: {
       week: 'week',
       day: 'day'
     },
     timeZone: 'UTC',
     initialView: 'dayGridMonth',
     editable: true,
     selectable: true,
     events: [{% for event in site.events %}{
       title  : '{{ event.title }}',
       url    : '{{ event.url }}',
       allDay : {% if event.all_day %}true{% else %}false{% endif %},
       {% unless event.end_date %}// {% endunless %}end    : '{{ event.end_date | date_to_xmlschema }}'
       start  : '{{ event.date | date_to_xmlschema }}'
      }{% if forloop.last %}{% else %},{% endif %}{% endfor %}
     ]
   });
  calendar.render();
});
</script>
