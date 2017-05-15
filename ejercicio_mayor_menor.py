#!/usr/bin/env python
# -*- coding: utf-8 -*-

v_a = input ("Introduzca el primer valor :")
v_b = input ("Introduzca el segundo valor :")
v_c = input ("Introduzca el tercer valor :")

if ( ( v_a == v_b and v_a == v_c ) or 
	 ( v_b == v_a and v_b == v_c ) or	
	 ( v_c == v_a and v_c == v_b ) ):
	
	print "No pueden haber numeros iguales!"

if (v_a > v_b and v_a > v_c):
	
	print "Gana el primer valor"
	
if (v_b > v_a and v_b > v_c):
	
	print "Gana el segundo valor"
	
if (v_c > v_a and v_c > v_b):
	
	print "Gana el tercer valor"

else: 
	
	print "Empate"
