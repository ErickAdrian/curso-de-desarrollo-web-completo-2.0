#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import random

print "Content-type: text/html; charset=utf-8"
print ""

rojos = 0
blancos = 0

form = cgi.FieldStorage()
if "respuesta" in form:
    respuesta = form.getvalue("respuesta")
else:
    respuesta = ""
    for i in range(4):
        respuesta = respuesta+str(random.randint(0,9))
    
if "adivina" in form:
    adivina = form.getvalue("adivina")
    # Comprobamos si ha acertado o no
    for indice, digito in enumerate(adivina):
        if digito == respuesta[indice]:
            rojos += 1
        else:
            for respuestaDigito in respuesta:
                if respuestaDigito == digito:
                    blancos+=1
                    break
else:
    adivina = ""
    

#print respuesta

if "intentos" in form:
    intentos = int(form.getvalue("intentos"))+1
else:
    intentos = 0
if intentos == 0:
    mensaje = "He escogido un número de 4 dígitos.¿Eres capaz de adivinarlo?"
elif rojos == 4:
    mensaje = "¡Enhorabuena!Lo conseguiste en " + str(intentos) + " intento(s)!.<a href=''>Jugar otra vez</a>"
else:
    mensaje = "Tienes " + str(rojos)+ " en el lugar correcto y "+str(blancos)+" en el lugar incorrecto. Llevas " + str(intentos)+ " intento(s)."
    
# Generacion de formulario para el usuario
print '<h1>Mastermind</h1>'
print '<p>' + mensaje + '</p>'
print '<form method="POST">'
print '<input type="text" name="adivina" value="' + adivina + '">'
print '<input type="hidden" name="intentos" value="' + str(intentos) + '">'
print '<input type="hidden" name="respuesta" value="' + respuesta + '">'
print '<input type="submit" value="Adivina!">'
print '</form>'