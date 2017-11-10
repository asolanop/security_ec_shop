#!/usr/bin/python3

import Helpers.db as db
import Helpers.structure as structure
import Helpers.nav as nav
import Helpers.myparser as parser
import os, sys

print("Content-Type: text/html\r\n\r\n")
db.connectDB()
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))

structure.printStartSection()
if autenticate != None :
	nav.printNav(autenticate, db.cartCount(autenticate))	
else :
	nav.printNav(autenticate)
structure.printSearchForm()
items = db.getAllItems()
structure.printItemContents(items, 1)
structure.printEndSection()
