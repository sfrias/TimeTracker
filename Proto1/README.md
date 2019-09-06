# First Prototype
First fit was Task, user id, register working time(start and stop), Site of working time, and %TaskPerformed last update.<br>
<br>
Create a prototype to register this absolute values related to working time:<br>
  1.- Select user id, to start, mark progress or complete specified task.
  2.- Select task of list that you were involved.<br>
  3.- Mark if , if this register is a start or an end for specified task.<br>
  4.- Mark Time in local time to convert after to UTC TZ simplified(Zulu), coded as UTF-8.<br>
  5.- Site code as enum of defined sites.<br>
  6.- Percentage of task performed on this local(Default= NULL, no changes).<br>
  7.- Mark if this work register would be local or updated to workgroup.<br>  
<br>
Other tests will be created too, as:<br>
  - Clean/process/tune localjournals<br>
  - First implementation for interprocess model between master/local journals.<br>
## Parts of prototype
Parts of prototype are:<br>
  1.- [Client](https://github.com/sfrias/TimeTracker/tree/master/Proto1/WebRcv)
      as application that can send an update to register on User TaskJournal, or receive info from other User Task Journals<br>
  2.- [Device](https://github.com/sfrias/TimeTracker/tree/master/Proto1/ServeForms)
      Task Journal: local device Agent for Task Journal.<br>
  3.- [Master](https://github.com/sfrias/TimeTracker/tree/master/Proto1/RoundRolling)
      User Task Journal: Personal Device that locally concentrates updates of all authorized user associated Task Journals.<br>
<br>
![Esquema1](https://github.com/sfrias/TimeTracker/blob/master/Proto1/Esquema01.jpg)
