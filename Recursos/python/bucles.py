#!/usr/bin/python
# -*- coding: utf-8 -*-

print "Content-type: text/html; charset=utf-8"
print ""

# Bucle for con funcion range(x)
for i in range(11):
    print i
    print " Curso Desarrollo Web Completo 2.0<br>"
    
# Bucle for con funcion range(x,y)
for i in range(5,11):
    print str(i) + "<br>"
    
comidasFavoritas = ["Chocolate", "Pizza", "Gazpacho", "Paella"]

for comida in comidasFavoritas:
    print "Me encanta comer " + comida + ".<BR>"
    
# Bucles while
x=1
while x<=10:
    print x
    x = x+1
print "Fin del bucle while"

# Iteracion sobre diccionarios
edades = {}
edades["Juan"] = 28
edades["Maria"] = 20
edades["Edwin"] = 10
edades["Priscila"] = 5

print "<BR><BR>"
for persona in edades:
    print persona + " tiene " + str(edades[persona]) + " años<br>"








