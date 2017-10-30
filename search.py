#!/usr/local/bin/python3

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
	autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))
	structure.printStartSection()
	nav.printNav(autenticate, db.cartCount(autenticate))
	structure.printSearchForm()
	item = parser.parseData(os.getenv("QUERY_STRING"))
	if validator.validateAplhaNumericEntry(item['search']) != None :
		data = db.search(item['search'])
		structure.printItemContents(data)
	else :
		print(""" <div> <p> The search string recieved unexpected characters. 
				Please enter only alphabetic characters </p> </div> """)
