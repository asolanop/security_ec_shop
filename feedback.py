#!/usr/local/bin/python3

import smtplib
import Helpers.myparser as parser
import Helpers.db as db
import os, sys
import Helpers.structure as structure
import Helpers.nav as nav

db.connectDB()
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))


def send_email(sender, firstname, lastname, body):
	recipient  = ['catsakumich@gmail.com']
	subject = "Feedback Mercadarte Birrero from %s" % (firstname + " " + lastname)
	gmail_user = ""
	gmail_pwd = ""
	TO = recipient if type(recipient) is list else [recipient]
	# Prepare actual message
	message = """From: %s\n
		     To: %s\n
                     Subject: %s\n\n%s
		  """ % (sender, ", ".join(TO), subject, body)
	print(message)	
	# The actual mail send
	try:	
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)		
		server.sendmail(gmail_user, recipient[0], message)		
		server.quit()
		print("Successfully sent email")
	except SMTPException:
		print("Error: unable to send email")


# Form to get feedback data 
print("Content-Type: text/html\r\n\r\n")
structure.printStartSection()
nav.printNav(autenticate, db.cartCount(autenticate))
print ("""<div>
	<h3>Enter your feedback:</h3>
	<form id="commentForm" method="POST">

	<label for="email">Your email*: </label>
	<input id="email" name="email" maxlength="50" type="text" /><br />
	
	<label for="firstname">Name*: </label>
	<input id="firstname" name="firstname" maxlength="25" type="text" /><br />
	
	<label for="lastname">Lastname*: </label>
	<input id="lastname" name="lastname" maxlength="25" type="text" /><br />
	<br/>
	<label for="comment">Your comment/doubt/feedback*: </label>
	<br/><br/>
	<textarea name="comment" form="commentForm">Enter text here...</textarea>	<br/>	

	<button id="submit">Submit</button>
	</form>
	<br>
	
	</div>""")

# Post method 
if os.getenv("REQUEST_METHOD") == 'POST':
	print("Content-Type: text/html\r\n\r\n")
	post_params = sys.stdin.read()	
	feed = parser.parseData(post_params)
	send_email(feed['email'], feed['firstname'], feed['lastname'], feed['comment'])

	print ("""\<div>
	<h2>Your comment was sent succesfully! 
	<a href="index.py">Go back to Home</a></h2>""")


