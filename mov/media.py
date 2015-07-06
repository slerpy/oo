#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# media.py
# --------------------
# Creating a class, movie.
#
# @author Slerpy, 0x899319D4251502BA
# @date  5 July 2015
# @version 0.0.1
##############################################################################

import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)