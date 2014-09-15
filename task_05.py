#!/usr/bin/env python
# -*- coding: utf-8 -*-

NAME = raw_input("What is your name")
PRINCIPAL = int(raw_input("What is the amount of your principal?"))
DURATION = int(raw_input("For how many years is this loan being borrowed?"))
PQ = raw_input("Are you pre-qualified for this loan (y/Yes/No/n)?").lower()[:1]
import decimal
if PRINCIPAL < 200000 and DURATION <= 15 and PQ == "y":
    IR = 363
elif PRINCIPAL < 200000 and DURATION <= 15 and PQ == "n":
    IR = 465
elif PRINCIPAL < 200000 and (DURATION > 15 and DURATION <= 20) and PQ == "y":
    IR = 404
elif PRINCIPAL < 200000 and (DURATION > 15 and DURATION <= 20) and PQ == "n":
    IR = 498
elif PRINCIPAL < 200000 and DURATION > 20 and PQ == "y":
    IR = 577
elif PRINCIPAL < 200000 and DURATION > 20 and PQ == "n":
    IR = 639
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and DURATION <= 15 and PQ == "y":
    IR = 302
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and DURATION <= 15 and PQ == "n":
    IR = 398
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and (DURATION > 15 and DURATION <= 20) and PQ == "y":
    IR = 327
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and (DURATION > 15 and DURATION <= 20) and PQ == "n":
    IR = 408
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and (DURATION > 20) and PQ == "y":
    IR = 466
elif PRINCIPAL <= 1000000 and DURATION <= 15 and PQ == "y":
    IR = 205
else:
    IR = 262
TOTAL = int(PRINCIPAL * ((1 + (IR / 10000) / 12)) ** (12 * DURATION))
REPORT = " Loan Report for: {0} \n---------------------------------------- \n	Principal: ${1}\n	Duration: {2}\n	Pre-qualified?: {3}\n \n	Total: ${4:8}".format(NAME, PRINCIPAL, DURATION, PQ, TOTAL)
print REPORT
