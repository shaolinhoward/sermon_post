#!/usr/bin/python

def read_msg_bundle(fn):
	with open(fn) as f:
		  lines = f.read().splitlines()

	varAr = {}
	for line in lines:
		if not line.startswith('#') and line.strip():
			lineAr = line.split("=")
			k = lineAr[0]
			v = lineAr[1]
			varAr[k] = v 
			
	return varAr
	
	f.close()
	
	
	
