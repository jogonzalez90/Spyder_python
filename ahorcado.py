# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:00:00 2022

@author: Asus pag 104
"""
import random

IMÁGENES_AHORCADO = ['''
                     
   ┌----
   |   
   |   
   |
   |
   |
 ▓▓▓▓▓▓▓▓▓''','''
                     
   ┌---┐
   |   
   |   
   |
   |
   |
 ▓▓▓▓▓▓▓▓▓''', '''
 
   ┌---┐
   |   O
   |   
   |    
   |
   |
 ▓▓▓▓▓▓▓▓▓''', '''
 
   ┌---┐
   |  <O
   |   
   |    
   |
   |
 ▓▓▓▓▓▓▓▓▓''','''
 
   ┌---┐
   |  <O>
   |   
   |    
   |
   |
 ▓▓▓▓▓▓▓▓▓''','''
 
   ┌---┐
   |  <O>
   |   |
   |   
   |
   |
 ▓▓▓▓▓▓▓▓▓''', '''
 
   ┌---┐
   |  <O>
   |  /|
   |  
   |
   |
 ▓▓▓▓▓▓▓▓▓''', '''
 
   ┌---┐
   |  <O>
   |  /|\ 
   |  
   |  
   |
 ▓▓▓▓▓▓▓▓▓''', '''

   ┌---┐
   |  <O>
   |  /|\ 
   |  /
   |  
   |
 ▓▓▓▓▓▓▓▓▓''', '''

   ┌---┐
   |  <O>
   |  /|\ 
   |  / \ 
   |  
   |
 ▓▓▓▓▓▓▓▓▓''']

#listaDePalabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

diccionarioDePalabras = {'Colores':'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(),
                   'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentagono hexagono heptagono octogono'.split(),
                   'Frutas':'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(),
                   'Animales':'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

#Funcion para devolver a azar un cadena de la lista palabras
def obtenerPalabraAlAzar(diccionarioDePalabras):
    claveDePalabras = random.choice(list(diccionarioDePalabras.keys()))
    índiceDePalabras = random.randint(0, len(diccionarioDePalabras[claveDePalabras])-1)
    return [diccionarioDePalabras[claveDePalabras][índiceDePalabras],[claveDePalabras]]
    #return índiceDePalabras

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()
  
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end='')
    print()
    
    espaciosVacíos = '_' * len(palabraSecreta)
    
    #Para espacios vacios con letras adivinadas
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
         
    #Visualiza la palabra secreta con espacios entre cada letra        
    for letra in espaciosVacíos:
        print(letra, end=' ')
    print()
    
def obtenerIntento(letrasProbadas):
    #Pasa letra ingresada por usuario. Verifica valor correcto
    while True:
        print('Ingrese una letra= ?. ')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('No se ha ingresado caracter, digitar letra. ')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra. ')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Caracter incorrecto, introduce una letra. ')
        else:
            return intento

#Funcion para continuar el juego     
def jugarDeNuevo():
    print('¿Quieres jugar de nuevo? (Sí o No).')
    return input().lower().startswith('s')

##############################
#### Programa principal ######
##############################    

print('''  Bienvenido... 
al juego "AHORCADO"
  en Python...''')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta, claveSecreta = obtenerPalabraAlAzar(diccionarioDePalabras)
if claveSecreta == ['Colores']:
    print('LA PALABRA SECRETA CORRESPONDE A COLORES')
elif claveSecreta == ['Formas']:
    print('LA PALABRA SECRETA CORRESPONDE A FORMAS')
elif claveSecreta == ['Frutas']:
    print('LA PALABRA SECRETA CORRESPONDE A FRUTAS')    
else:
    print('LA PALABRA SECRETA CORRESPONDE A ANIMALES')
juegoTerminado = False

while True:
    #print('La palabra secreta pertenece al conjunto: "' + claveSecreta + '"')
    #print('La palabra secreta pertenece al conjunto: ' + claveSecreta)
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    #Ingreso de tecla
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
   
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        
        #Deteminar si el jugador ha ganado
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras == True:
    
             print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
             juegoTerminado = True
             
    else:
        letrasIncorrectas = letrasIncorrectas + intento
        
        #Verifica los intentos del jugador
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos !\nDespués de ' + str(len(letrasIncorrectas)) +' intentos fallidos y '+ str(len(letrasCorrectas)) +' aciertos, la palabra secreta era: "' + palabraSecreta +'"')
            juegoTerminado = True
            
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta, claveSecreta = obtenerPalabraAlAzar(diccionarioDePalabras)
            if claveSecreta == ['Colores']:
                print('LA PALABRA SECRETA CORRESPONDE A COLORES')
            elif claveSecreta == ['Formas']:
                print('LA PALABRA SECRETA CORRESPONDE A FORMAS')
            elif claveSecreta == ['Frutas']:
                print('LA PALABRA SECRETA CORRESPONDE A FRUTAS')    
            elif claveSecreta == ['Animales']:
                print('LA PALABRA SECRETA CORRESPONDE A ANIMALES')
        else:
            break

















