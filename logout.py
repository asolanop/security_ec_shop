#!/usr/local/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import os, sys, time
from datetime import datetime, timedelta

# print("Content-Type: text/html\r\n\r\n")

db.connectDB()
cookie = parser.parseCookie(os.getenv("HTTP_COOKIE"))
autenticate = db.checkSession(cookie)
if autenticate != None :
	db.delSession(cookie['SessionID'])

print("Set-Cookie: SessionID=''; Expires=" + time.strftime("%a, %d %b %Y %T GMT") + ";")
print("Set-Cookie: Expires=''; Expires=" + time.strftime("%a, %d %b %Y %T GMT") + ";")
#print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py") 
#print("Location: http://localhost/index.py")
print()

print("Succesfully logged out!") #Borrar al descomentar el Location
