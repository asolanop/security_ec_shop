#!/usr/bin/python3

import Helpers.db as db
import Helpers.myparser as parser
import os, sys
import Helpers.validator as validator
import Helpers.structure as structure
import Helpers.nav as nav


db.connectDB()
cookie = parser.parseCookie(os.getenv("HTTP_COOKIE"))
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE"))) if validator.validateSession(cookie) else None
if autenticate != None :
	referer = os.getenv("HTTP_REFERER")
	cartItem = parser.parseData(sys.stdin.read())
	result = db.addToCart(cartItem['itemID'], autenticate)	
	if result == None :
		#Error agregando el item
		print("Content-Type: text/html\r\n\r\n")
		structure.printStartSection()
		nav.printNav(autenticate, db.cartCount(autenticate))
		print("Error agregando al carrito. Intentelo de nuevo (refresque el sitio) </br> ")
		print('<a href="' + referer + '" > Regresar a la p&aacute;gina anterior.')
	else :
		#Redirect a la pagina anterior
		print("Location: " + referer)
		print()
else :
	#Redirect a LOGIN
	#print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/login.py")	
	print("Location: https://172.24.129.8/login.py")
	print()

	
