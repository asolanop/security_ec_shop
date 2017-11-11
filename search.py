#!/usr/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import Helpers.structure as structure
import Helpers.nav as nav
import Helpers.validator as validator
import os, sys

print("Content-Type: text/html\r\n\r\n")

#print(os.getenv("QUERY_STRING"))
#print(os.getenv("REQUEST_METHOD"))

if os.getenv("REQUEST_METHOD") == 'GET':
	db.connectDB()
	cookie = parser.parseCookie(os.getenv("HTTP_COOKIE"))
	autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE"))) if validator.validateSession(cookie) else None
	structure.printStartSection()
	nav.printNav(autenticate, db.cartCount(autenticate))
	structure.printSearchForm()
	item = parser.parseData(os.getenv("QUERY_STRING"))
	if validator.validateEntryLenght(item['search'], 1, 50) and validator.validateAplhaNumericEntry(item['search']) != None :
		data = db.search(item['search'])
		structure.printItemContents(data, 1)
	else :
		print(""" <div> <p> The search string recieved unexpected characters. 
				Please enter only alphabetic characters </p> </div> """)
