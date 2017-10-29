#!/usr/bin/python3.6
from urllib import parse


def parseData(rawUser):
	userData = parse.unquote_plus(rawUser).split("&")
	dict = {}
	for attribute in userData:
		tokens = attribute.split("=")
		dict[tokens[0]] = tokens[1]
	return dict

def parseCookie(cookie):
	if cookie != None:
		cookieData = cookie.split(";")
		dict = {}
		for attribute in cookieData:
			tokens = attribute.split("=")
			dict[tokens[0].strip()] = tokens[1].strip()
		return dict
	return None

def a():
	print("Hola andru")
