#!/usr/bin/env python
# -*- coding: utf-8 -*-

for fila in xrange (1,6,1):
	for col in xrange (1,5,1):
	
		if fila == 1 and col == 3:
			print "*", ""
		
		if fila == 2 and col == 3:
			print "A", ""
		
		if((fila == 3 and col == 1) or 
		   (fila == 3 and col == 5)):
			print "", ""
		
		else: 
			print "A", ""
			
		if fila == 4:
			print "A", ""
			
		if fila == 5 and col == 3:
			
			print "N", ""
			
		if fila == 6 and col == 3:
			
			print "N", ""
		
	print "",
