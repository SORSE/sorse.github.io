---
title: Calendar
permalink: /programme/calendar/
sidebar: 
  nav:  programme
classes: wide
toc: true
toc_sticky: true
---


<link rel='stylesheet' type='text/css' href="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.6/fullcalendar.min.css" />

<div id='calendar'></div>

<script src='https://code.jquery.com/jquery-1.11.2.min.js'></script>
<script src='https://code.jquery.com/ui/1.11.2/jquery-ui.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.9.0/moment.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.6/fullcalendar.min.js'></script>

<script>
$(document).ready(function() {
   $('#calendar').fullCalendar({
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    initialView: "dayGridMonth"
  });

//  var dateStr = "2020-06-30";
//  var date = new Date(dateStr + 'T00:00:00'); // will be in local time
//  calendar.addEvent({
//    title: 'dynamic event',
//    start: date,
//    allDay: true
//  });
//  calendar.render();
});
</script>
