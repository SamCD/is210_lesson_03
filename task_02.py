#!/usr/bin/env python
# -*- coding: utf-8 -*-

BP = int(raw_input("What is your blood pressure?"))
if BP <= 89:
    BP_STATUS = "Low"
elif BP <= 119:
    BP_STATUS = "Ideal"
elif BP <= 139:
    BP_STATUS = "Warning"
elif BP <= 159:
    BP_STATUS = "High"
else:
    BPSTATUS = "Emergency"
STATEMENT = "Your blood pressure is at a level of {0}".format(BP_STATUS)
