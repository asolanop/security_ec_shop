#!/usr/local/bin/python3

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
	return True

def validateSession(entry):
	return True

def validateUser(user):
	fname_res = validateStringOnlyEntry(user['firstname'])
	lname_res = validateStringOnlyEntry(user['lastname'])
	pass_res = validateSpecialStringEntry(user['password'])
	username_res = validateAplhaNumericEntry(user['username'])
	tel_res = validateNumber(user['telephone'])
	adr_res = validateSpecialStringEntry(user['address'])
	email_res = validateMail(user['email'])
	if(fname_res == None): return 2
	if(lname_res == None): return 2
	if(pass_res == None): return 3
	if(username_res == None): return 4
	if(tel_res == None): return 5
	if(adr_res == None): return 6
	if(email_res == None): return 7
	return True

def validateLogin(intent):
	pass_res = validateSpecialStringEntry(intent['password'])
	username_res = validateAplhaNumericEntry(intent['username'])
	if(pass_res == None): return False
	if(username_res == None): return False
	return True


	
	
