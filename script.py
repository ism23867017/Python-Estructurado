#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


for root, dirs, files in os.walk("Documentos"):
	
	for name in files:
		
		name_path = os.path.join(root, name)
		print name_path
		print len(name_path), "b"
		
		
		
