#!/usr/bin/env python
# -*- coding: utf-8 -*-

NAME = raw_input("What is your name")
PRINCIPAL = int(raw_input("What is the amount of your principal?"))
DURATION = int(raw_input("For how many years is this loan being borrowed?"))
PQ = raw_input("Are you pre-qualified for this loan (y/Yes/No/n)?").lower()[:1]
import decimal
if PRINCIPAL < 200000 and DURATION <= 15 and PQ == "y":
    IR = decimal.Decimal(3.63)
elif PRINCIPAL < 200000 and DURATION <= 15 and PQ == "n":
    IR = decimal.Decimal(4.65)
elif PRINCIPAL < 200000 and (DURATION > 15 and DURATION <= 20) and PQ == "y":
    IR = decimal.Decimal(4.04)
elif PRINCIPAL < 200000 and (DURATION > 15 and DURATION <= 20) and PQ == "n":
    IR = decimal.Decimal(4.98)
elif PRINCIPAL < 200000 and DURATION > 20 and PQ == "y":
    IR = decimal.Decimal(5.77)
elif PRINCIPAL < 200000 and DURATION > 20 and PQ == "n":
    IR = decimal.Decimal(6.39)
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and DURATION <= 15 and PQ == "y":
    IR = decimal.Decimal(3.02)
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and DURATION <= 15 and PQ == "n":
    IR = decimal.Decimal(3.98)
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and (DURATION > 15 and DURATION <= 20) and PQ == "y":
    IR = decimal.Decimal(3.27)
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and (DURATION > 15 and DURATION <= 20) and PQ == "n":
    IR = decimal.Decimal(4.08)
elif (PRINCIPAL >= 200000 and PRINCIPAL < 1000000) and (DURATION > 20) and PQ == "y":
    IR = decimal.Decimal(4.66)
elif PRINCIPAL <= 1000000 and DURATION <= 15 and PQ == "y":
    IR = decimal.Decimal(2.05)
else:
    IR = decimal.Decimal(2.62)
TOTAL = int(PRINCIPAL * ((1 + ((IR/100) / 12)) ** (12 * DURATION)))
REPORT = " Loan Report for: {0} \n---------------------------------------- \n	Principal: ${1}\n	Duration: {2}\n	Pre-qualified?: {3}\n \n	Total: ${4:8}".format(NAME, PRINCIPAL, DURATION, PQ, TOTAL)
print REPORT
