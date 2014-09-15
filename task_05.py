#!/usr/bin/env python
# -*- coding: utf-8 -*-

NAME = raw_input("What is your name")
PRINCIPAL = int(raw_input("What is the amount of your principal?"))
DURATION = int(raw_input("For how many years is this loan being borrowed?"))
PQ = raw_input("Are you pre-qualified for this loan (y/Yes/No/n)?")
if PRINCIPAL < 200000 and DURATION <= 15:
