#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# word_filter.py
# --------------------
# A program to scan for profanity.
#
# @author Slerpy, 0x899319D4251502BA
# @date  4 July 2015
# @version 0.0.1
##############################################################################

import urllib


def read_text():
    quotes = open("/path/to/file/to/scan/")     # Enter path to document we'll be scanning for language
    contents_of_file = quotes.read()            # load up words to scan
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check) # using wdyls check so we dont have to make our own.
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Noope, Your language runs afoul of arbitrary societal norms.")
    elif "false" in output:
        print("All clear. Send it.")
    else:
        print("Error Error Error, something is wrong.")

read_text()