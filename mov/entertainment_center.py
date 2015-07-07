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

import fresh_tomatoes
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

the_breakfast_club = media.Movie("The Breakfast Club",
                                 "Five teenagers, each a member of a different high school clique, who spend a Saturday in detention together and come to realize that they are all more than their respective stereotypes, while facing a villainous principal.",
                                 "https://upload.wikimedia.org/wikipedia/en/5/50/The_Breakfast_Club.jpg",
                                 "https://www.youtube.com/watch?v=9iQOw0dHRZA")

wild = media.Movie("Wild",
                   "With absolutely no experience, driven only by sheer determination, Cheryl hikes more than a thousand miles of the Pacific Crest Trail, alone.",
                   "https://upload.wikimedia.org/wikipedia/en/3/37/Wild2014Poster.jpg",
                   "https://www.youtube.com/watch?v=tn2-GSqPyl0")

the_imitation_game = media.Movie("The Imitation Game,",
                                 "British authorities entered the home of mathematician, cryptanalyst and war hero Alan Turing (Benedict Cumberbatch) to investigate a reported burglary. They instead ended up arresting Turing himself on charges of 'gross indecency', an accusation that would lead to his devastating conviction for the criminal offense of homosexuality - little did officials know, they were actually incriminating the pioneer of modern-day computing.",
                                 "http://www.filmmusicnotes.com/wp-content/uploads/2015/01/imitation_game.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")

movies = [toy_story, avatar, annie_hall, the_breakfast_club, wild, the_imitation_game]
fresh_tomatoes.open_movies_page(movies)
