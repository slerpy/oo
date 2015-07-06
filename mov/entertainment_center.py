#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# entertainment_center.py
# --------------------
# The list of movies to test our Media class.
#
# @author Slerpy, 0x899319D4251502BA
# @date  5 July 2015
# @version 0.0.1
##############################################################################

import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys which come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A Marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

annie_hall = media.Movie("Annie Hall",
                         "Examining the rise and fall of relationships.",
                         "https://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg",
                         "https://www.youtube.com/watch?v=TBzHphcc2Jw")

annie_hall.show_trailer()
# avatar.show_trailer()
