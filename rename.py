#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# rename.py
# --------------------
# A simple file renaming script
#
# @author slerpy, 0x899319D4251502BA
# @date 22 June 2015
# @version 0.0.1
##############################################################################

import os

## which folder contains the files we're going to rename? path goes between " "
files_location = r"/path/to/folder/with/files/to/rename"


def rename_files():
    file_ls = os.listdir(files_location)    # grab files list
    os.chdir(files_location)                # change to folder with files in order to start our rename.


    for file_name in file_ls:               # for through and remove any numbers or dashes from file names.
        print ("Renaming " + file_name + "to " + file_name.translate(None, "0123456789-")) # be verbose.
        os.rename(file_name, file_name.translate(None, "0123456789-"))

rename_files()