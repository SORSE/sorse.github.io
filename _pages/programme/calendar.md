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
     events: 'https://fullcalendar.io/demo-events.json',
     editable: true,
     selectable: true
   });
  calendar.render();
});
</script>
