#!/usr/bin/python
# -*- coding: utf-8 -*-

print "Content-type: text/html; charset=utf-8"
print ""

# Para definir una funcion en Python
def decirHola():
    print "Hola"

decirHola()

def decirAlgo(algo):
    print algo

decirAlgo("Hola a todos desde Python!")

def multiplicarDosNumeros(x,y):
    return x*y

print multiplicarDosNumeros(30,2)

# Funcion Máximo Común Divisor
def MaximoComunDivisor(x,y):
    MCD = 1
    for i in range(1,x+1):
        if x % i == 0 and y % i == 0:
            MCD = i
    return MCD

print MaximoComunDivisor(60,12)


a = 5
b = 6

def sumaDosNumeros():
    a = 10
    return a + b

print sumaDosNumeros()
print a