#!/usr/bin/env python
# -*- coding: utf-8 -*-

BASE = raw_input("What is your base color?")
if BASE == "Seattle Gray":
   ACCENT = raw_input("What is your accent, Ceramic Glaze or Cumulus Nimbus?")
   if ACCENT == "Ceramic Glaze":
      HIGHLIGHT = raw_input("What is your highlight, Basically White or White?")
   elif ACCENT == "Cumulus Nimbus":
      HIGHLIGHT = raw_input("What is your highlight, Off-White or Paper White?")
elif BASE == "Manatee":
   ACCENT = raw_input("What is your accent, Platinum Mist or Spartan Sage?")
   if ACCENT == "Platinum Mist":
      HIGHLIGHT = raw_input("WHat is your highlight, Bone White or Just White?")
   elif ACCENT == "Spartan Sage":
      HIGHLIGHT = raw_input("What is your highlight, Fractal White or Not White?")
MESSAGE = "You have selected {0}, {1} and {2}".format(BASE, ACCENT, HIGHLIGHT)
print MESSAGE
