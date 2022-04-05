# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:02:55 2020

@author: Asus
"""

import turtle
import random


pat = turtle.Turtle()

turtle.Screen().bgcolor("blue")
colours = ["red", "black", "white", "yellow"]
pat.color("black")

"""
pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()
"""

for i in range(10):
    for i in range(2):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
    pat.right(36)
    pat.color(random.choice(colours))