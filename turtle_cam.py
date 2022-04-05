# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:27:03 2020

@author: Asus
"""

from turtle import*
from random import randint


speed(0)#velocidad de imprecion pista
penup()#bajamos pluma para escritura
goto(-140, 140)#punto de inicio en lienzo


for step in range(20):#ciclo for para trazado pista
    write(step, align='center')#centrado de numeros en trazos
    right(90)#rotar 90 grados
    forward(10)#avanza 10 unidades
    pendown()#lavantar pluma de lienzo
    forward(180)#avanza 180 unidades
    penup()#baja pluma
    backward(190)#retrocede unidades
    left(90)#rota 90 grados a la izquierda
    forward(20)#avanza 20 unidades
    
ada= Turtle()#creacion de tortuga
ada.color('yellow')#asigna color
ada.shape('turtle')#forma

ada.penup()#baja pluma de tortuga
ada.goto(-160, 100)#punto de partida ubicacion
ada.pendown()#levanta pluma

bob= Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

cat= Turtle()
cat.color('red')
cat.shape('turtle')

cat.penup()
cat.goto(-160, 40)
cat.pendown()

ang= Turtle()
ang.color('purple')
ang.shape('turtle')

ang.penup()
ang.goto(-160, 10)
ang.pendown()

jon= Turtle()
jon.color('black')
jon.shape('turtle')

jon.penup()
jon.goto(-160, -20)
jon.pendown()

for turn in range(10):#GIRAN TODAS LAS TORUGAS PRESUMIENDO 360 grados
    ada.right(36)
    bob.left(36)
    cat.right(36)
    jon.left(36)
    ang.right(36)

for turn in range(50):#avance de tortugas
    ada.penup()#baja plumas
    bob.penup()
    cat.penup()
    ang.penup()
    jon.penup()
    ada.forward(randint(1,7))#anvanza un numero aleatorio enter 1 y 7
    bob.forward(randint(1,7))
    cat.forward(randint(1,7))
    jon.forward(randint(1,7))
    ang.forward(randint(1,7))
    ada.pendown()#lavanta plumas
    bob.pendown()
    cat.pendown()
    ang.pendown()
    jon.pendown()
    ada.forward(randint(1,7))#anvanza un numero aleatorio enter 1 y 7
    bob.forward(randint(1,7))
    cat.forward(randint(1,7))
    jon.forward(randint(1,7))
    ang.forward(randint(1,7))
    
    
   
    

    
    
    
    
    
    
    
