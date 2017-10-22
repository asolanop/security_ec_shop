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
nav.printNav(autenticate)
items = db.getAllItems()
structure.printItemContents(items)
structure.printEndSection()

