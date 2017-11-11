#!/usr/local/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import Helpers.validator as validator
import os, sys, time
from datetime import datetime, timedelta

db.connectDB()
cookie = parser.parseCookie(os.getenv("HTTP_COOKIE"))
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE"))) if validator.validateSession(cookie) else None
if autenticate != None :
	db.delSession(cookie['SessionID'])

print("Set-Cookie: SessionID=''; Expires=" + time.strftime("%a, %d %b %Y %T GMT") + ";")
print("Set-Cookie: Expires=''; Expires=" + time.strftime("%a, %d %b %Y %T GMT") + ";")
print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py") 
#print("Location: http://localhost/index.py")
print()

#print("Succesfully logged out!") #Borrar al descomentar el Location
