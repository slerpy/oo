#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# break_time.py
# --------------------
# Break timer.
#
# @author Slerpy, 0x899319D4251502BA
# @date 21 June 2015
# @version 0.0.1
##############################################################################

import time
import webbrowser


total_breaks = 3            # how many breaks throughout the day?
breaks_taken = 0            # how many breaks have we taken on this loop through?
time_between_breaks = 7200    # How long between each break? measured in seconds. 7200 == 2 hours.
url_to_load = "https://www.youtube.com/watch?v=3ez0daDsx_I" # what website will be loading to initiate a break?

print("Break timer started @ "+time.ctime())
while breaks_taken < total_breaks:        # each time we take a break, add one to breaks_taken until we reach total_breaks.
    time.sleep(time_between_breaks)
    webbrowser.open(url_to_load)
    breaks_taken = breaks_taken + 1
    print("Break #" + str(breaks_taken) + " initiated.")
