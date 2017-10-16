#!/usr/bin/python3

import Helpers.db
import Helpers.structure

def printHeaders():
	print("Content-Type: text/html\r\n\r\n")

def createHomeBody():
	#Helpers.db.init()
	items = Helpers.db.getAllItems()
	Helpers.structure.printItemContents(items)

printHeaders()
Helpers.structure.printStartSection()
createHomeBody()
Helpers.structure.printEndSection()
