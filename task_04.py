#!/usr/bin/env python
# -*- coding: utf-8 -*-

DAY = raw_input("What day is it today?")[:3]
TIME = raw_input("What time is it in format hhmm?")
if (DAY.lower() == "sat" or DAY.lower() == "sun") or (TIME < 0600):
       SNOOZE = True
else:
       SNOOZE = False
if SNOOZE == False:
       print "Beep! Beep! Beep! Beep! Beep!"
