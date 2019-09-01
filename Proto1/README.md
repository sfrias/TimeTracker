First fit was register working time(start and stop), Site of working time, and %TaskPerformed last update.


Create a prototype to register this absolute values related to working time:
  1.- Start of Working Time in UTC TZ simplified(Zulu), coded as UTF-8.
  2.- Stop of Working Time in UTC TZ simplified(Zulu), coded as UTF-8.
  3.- Site code as enum of defined sites (default = 0 that's worker location).
  4.- Percentage of task performed on this update(Default= NULL, no changes).

Parts of prototype are:
  1.- Client as application that can send an update to register on User TaskJournal, or receive info from other User Task Journals
  2.- Device Task Journal: local device Agent for Task Journal.
  3.- Master User Task Journal: Personal Device that locally concentrates updates of all authorized user associated Task Journals.
  
