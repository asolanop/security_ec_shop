#!/usr/local/bin/python3
import urllib

def parse(rawUser):
	userData = urllib.unquote(rawUser).split("&")
	dict = {}
	for attribute in userData:
		tokens = attribute.split("=")
		dict[tokens[0]] = tokens[1]
	return dict

def a():
	print("Hola andru")