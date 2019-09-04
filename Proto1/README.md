First fit was Task, user id, register working time(start and stop), Site of working time, and %TaskPerformed last update.<br>
<br>
<br>
Create a prototype to register this absolute values related to working time:<br>
  1.- Start of Working Time in UTC TZ simplified(Zulu), coded as UTF-8.<br>
  2.- Stop of Working Time in UTC TZ simplified(Zulu), coded as UTF-8.<br>
  3.- Site code as enum of defined sites (default = 0 that's worker location).<br>
  4.- Percentage of task performed on this update(Default= NULL, no changes).<br>

Parts of prototype are:<br>
  1.- Client as application that can send an update to register on User TaskJournal, or receive info from other User Task Journals<br>
  2.- Device Task Journal: local device Agent for Task Journal.<br>
  3.- Master User Task Journal: Personal Device that locally concentrates updates of all authorized user associated Task Journals.<br>
  
