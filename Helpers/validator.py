#!/usr/bin/python3

import re

def validateStringOnlyEntry(entry):
	pattern = re.compile("^([a-zA-Z ])+$")
	#print(pattern.match(entry))
	return pattern.match(entry)

def validateAplhaNumericEntry(entry):
	pattern = re.compile("^([a-zA-Z0-9 ])+$")
	#print(pattern.match(entry))
	return pattern.match(entry)

def validateSpecialStringEntry(entry):
	pattern = re.compile("^([a-zA-Z0-9_,\.\-\*\? ])+$")
	#print(pattern.match(entry))
	return pattern.match(entry)

def validateMail(entry):
	pattern = re.compile("^([a-zA-Z0-9_\-\.])+@([a-zA-Z\.])+$")
	#print(pattern.match(entry))
	return pattern.match(entry)

def validateNumber(entry):
	pattern = re.compile("^([0-9,\.])+$")
	#print(pattern.match(entry))
	return pattern.match(entry)

def validateEntryLenght(entry, min_lenght, max_lenght):
	if((len(entry) >= min_lenght) and (len(entry) <= max_lenght)):
		return True
	return False

def validateSession(entry):
	if ((entry == None) or (not ('SessionID' in entry))): return False
	if(not(validateEntryLenght(entry['SessionID'], 32 , 32))): return False
	pattern = re.compile("^([a-f0-9])+$")
	if(pattern.match(entry['SessionID']) == None) : return False
	return True

def validateUser(user):
	fname_res = validateStringOnlyEntry(user['firstname'])
	lname_res = validateStringOnlyEntry(user['lastname'])
	pass_res = validateSpecialStringEntry(user['password'])
	username_res = validateAplhaNumericEntry(user['username'])
	tel_res = validateNumber(user['telephone'])
	adr_res = validateSpecialStringEntry(user['address'])
	email_res = validateMail(user['email'])
	if(not(validateEntryLenght(user['firstname'], 1, 50)) and fname_res == None): return 2
	if(not(validateEntryLenght(user['lastname'], 1, 50)) and lname_res == None): return 2
	if(not(validateEntryLenght(user['password'], 8, 16)) and pass_res == None): return 3
	if(not(validateEntryLenght(user['username'], 1, 25)) and username_res == None): return 4
	if(not(validateEntryLenght(user['telephone'], 8, 12)) and tel_res == None): return 5
	if(not(validateEntryLenght(user['address'], 1, 50)) and adr_res == None): return 6
	if(not(validateEntryLenght(user['email'], 1, 75)) and email_res == None): return 7
	return True

def validateItem(item):
	item_name = validateAplhaNumericEntry(item['name'])
	item_descrip = validateSpecialStringEntry(item['description'])
	item_price = validateNumber(item['price'])
	if(not(validateEntryLenght(item['name'], 1, 25)) and item_name == None): return 2
	if(not(validateEntryLenght(item['description'], 1, 100)) and item_descrip == None): return 2
	if(not(validateEntryLenght(item['price'], 1, 15)) and item_price == None): return 3
	return True

def validateLogin(intent):
	pass_res = validateSpecialStringEntry(intent['password'])
	username_res = validateAplhaNumericEntry(intent['username'])
	if(not(validateEntryLenght(intent['password'], 8, 16)) or pass_res == None): return False
	if(not(validateEntryLenght(intent['username'], 1, 25)) or username_res == None): return False
	return True

def validateAddress(deliveryAddress):
	result = validateSpecialStringEntry(deliveryAddress['address'])
	if(not(validateEntryLenght(deliveryAddress['address'], 1, 50)) and result == None): return False
	return True
	
	
