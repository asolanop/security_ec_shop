#!/usr/local/bin/python3

import Helpers.db as db
import Helpers.myparser as parser
import os, sys


db.connectDB()
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))
if autenticate != None :
	referer = os.getenv("HTTP_REFERER")
	cartItem = parser.parseData(sys.stdin.read())
	result = db.addToCart(cartItem['itemID'], autenticate)	
	if result == None :
		print("Content-Type: text/html\r\n\r\n")
		print("Error agregando al carrito. Intentelo de nuevo: ")
		print('<a href="' + referer + '" > Regresar a la p&aacute;gina anterior.')
	else :
		print("Content-Type: text/html\r\n\r\n")
		print("Redirect a: " + referer)

#else :
	
