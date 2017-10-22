#!/usr/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import Helpers.structure as structure
import Helpers.nav as nav
import os, sys

print("Content-Type: text/html\r\n\r\n")

#print(os.getenv("QUERY_STRING"))
#print(os.getenv("REQUEST_METHOD"))

if os.getenv("REQUEST_METHOD") == 'GET':
	db.connectDB()
	autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))
	structure.printStartSection()
	nav.printNav(autenticate)
	item = parser.parseData(os.getenv("QUERY_STRING"))
	data = db.search(item['search'])
	structure.printItemContents(data)
