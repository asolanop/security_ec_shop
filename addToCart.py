#!/usr/bin/python3.6

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
		#Error agregando el item
		print("Content-Type: text/html\r\n\r\n")
		print("Error agregando al carrito. Intentelo de nuevo (refresque el sitio) </br> ")
		print('<a href="' + referer + '" > Regresar a la p&aacute;gina anterior.')
	else :
		#Redirect a la pagina anterior
		print("Location: " + referer)
		print()
else :
	#Redirect a LOGIN
	print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/login.py")	
	#print("Location: http://localhost/login.py")
	print()

	
