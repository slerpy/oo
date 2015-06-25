#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# stormy.py
# --------------------
# shapes with turtle
#
# @author Slerpy, 0x899319D4251502BA
# @date 24 June 2015
# @version 0.0.1
##############################################################################

import turtle


def go_square(a_turtle): #draw our square
    for i in range (1,5):
        a_turtle.forward(100)
        a_turtle.right(90)

def artsies():
    window = turtle.Screen()    # opens a window for our turtles to draw on
    window.bgcolor("red")       # sets the window background to red

    herman = turtle.Turtle()        # if I had a pet turtle, his name would be herman
    herman.shape("turtle")          # and i would like him to be shaped like a turtle
    herman.color("yellow")          # with hints of yellow on his shell
    herman.speed(2)                 # and be a little faster than a speed(1) turtle

    for i in range(1,54):
        go_square(herman)               # i would train him to walk in a square.
        herman.right(7.5)

    # mildred = turtle.Turtle()       # if i had a second turtle, i would probably name her mildred
    # mildred.shape("circle")         # her shell would be like a sphere
    # mildred.color("blue")           # with beautiful hints of a nice shade of blue
    # mildred.circle(100)             # she'd be doomed to walk in a circle boohoo.
    #
    window.exitonclick()            # and with a single click their world would come crashing down.

artsies()
