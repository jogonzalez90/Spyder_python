# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:52:28 2020

@author: Asus
"""

import turtle

import random

pat = turtle.Turtle()

turtle.Screen().bgcolor("blue")
colours = ["red", "black", "white", "yellow"]

pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            pat.color(random.choice(colours))
            pat.forward(30)
            
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
        #pat.color(random.choice(colours))
    pat.right(90)
    pat.color(random.choice(colours))
    pat.forward(90)
    #pat.color(random.choice(colours))
    
for i in range(8):
    branch()
    pat.left(45)
