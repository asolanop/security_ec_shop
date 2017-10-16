#!/usr/local/bin/python3
from urllib import parse


def parseData(rawUser):
	userData = parse.unquote(rawUser).split("&")
	dict = {}
	for attribute in userData:
		tokens = attribute.split("=")
		dict[tokens[0]] = tokens[1]
	return dict

def a():
	print("Hola andru")
