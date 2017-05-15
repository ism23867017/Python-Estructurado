#!/usr/bin/env python
# -*- coding: utf-8 -*-


salir = False

while salir == False:
	print "1-Sumar"
	print "2-Restar"
	print "3-Multiplicar"
	print "4-Dividir"
	print "0-Salir"
	opcionmain = input("Seleciona la opcion deseada: ")

	if opcionmain == 1:
		
		s1 = input("Introduzca la primera cifra: ")
		s2 = input("Introduzca la segunda cifra: ")
		print "El resultado es ", s1 + s2
	
	if opcionmain == 2:
		
		s1 = input("Introduzca la primera cifra: ")
		s2 = input("Introduzca la segunda cifra: ")
		print "El resultado es ", s1 - s2
	
	if opcionmain == 3:
		
		s1 = input("Introduzca la primera cifra: ")
		s2 = input("Introduzca la segunda cifra: ")
		print "El resultado es ", s1 * s2
	
	if opcionmain == 4:
		
		s1 = input("Introduzca la primera cifra: ")
		s2 = input("Introduzca la segunda cifra: ")
		print "El resultado es ", s1 / s2
	
	if opcionmain == 0:
		
		salir = True
	
