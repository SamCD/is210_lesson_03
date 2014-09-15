#!/usr/bin/env python
# -*- coding: utf-8 -*-

DAY = raw_input("What day is it today?")[:4]
TIME = raw_input("What time is it in format hhmm?")
if (DAY.lower == "sat" or DAY.lower == "sun") or (TIME < 0600):
       SNOOZE = True
else:
       SNOOZE = False
if SNOOZE == False:
       ALARM = "Beep! Beep! Beep! Beep! Beep!"
print ALARM
