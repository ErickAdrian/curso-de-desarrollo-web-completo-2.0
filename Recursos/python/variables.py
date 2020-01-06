#!/usr/bin/python
# -*- coding: utf-8 -*-

print "Content-type: text/html; charset=utf-8"
print ""
#############
# Variables
#############

edad = 20
print edad
pi = 3.14159
resultado = edad * pi
print resultado
cadena1 = "Mi nombre es José Luis"
print cadena1
cadena2 = " y soy desarrollador de Python"
cadenaConcatenada = cadena1 + cadena2
print cadenaConcatenada
print "<br><br>"
numero = "5"
print float(numero)*edad
print "<br><br>"
print cadenaConcatenada[0:9]
print "<br><br>"
print cadena1[-10:]

######## Arrays ############
print "<br><br>"
lista = ["Penelope", "Antonio", "Pepe", "Jose Luis"]

print lista
print lista[0]
print lista[1]
print lista[1:4]
print lista[-1]
lista[3] = "JL"
print lista

######## Tuplas ###########
miTupla = (1,2,3,4,5)
print "<br><br>"
print miTupla
print miTupla[0]
print miTupla[2]

######## Diccionarios ########
diccionario = {}
diccionario["papa"] = "Jose Luis"
diccionario["mama"] = "Penelope"
print diccionario["papa"] + " y " + diccionario["mama"]
print diccionario.keys()
print diccionario.values()








