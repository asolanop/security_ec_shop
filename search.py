#!/usr/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import Helpers.structure
import os, sys

print("Content-Type: text/html\r\n\r\n")
print("antes de todo")
print(os.getenv("QUERY_STRING"))
print(os.getenv("REQUEST_METHOD"))
if os.getenv("REQUEST_METHOD") == 'GET':
	item = parser.parseData(os.getenv("QUERY_STRING"))
	print(item['search'])
	db.connectDB()
	data = db.search(item['search'])
	Helpers.structure.printItemContents(data)
