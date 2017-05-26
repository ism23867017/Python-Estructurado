#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import stat
path_to_explore="Documentos"


for root, dirs, files in os.walk(path_to_explore):
	
	for name in files:
		
		name_path = os.chmod(path_to_explore, stat.S_IRWXO)
		
print "Has cambiado los permisos de:", path_to_explore
