#!/usr/bin/python3

import Helpers.db

def printHeaders():
	print("Content-Type: text/html\r\n\r\n")

def printStartSection():
	print("<html>")
	print("<head><title> El Mercadito Musical </title> </head>")
	
def printHomeBody():
	print("<body>")
	print("<h2>El Mercadito Musical</h2>")
	bigtempl = '''<center>
        		<table border="0" cellspacing="15">
        			{rows}
        		</table>
    		</center>'''

	rowtempl = """
	<tr>
	    <td align="center" style="font-size:1.25em;">
	    <p class="sansserif"> <b> Number: {number:d} </b> <br>
	    Letter: {letter} </p>
	    </td>
	</tr>
	"""
	numbers = [0, 1, 2, 3]
	letters = ["A", "B", "C", "D"]

	lst = zip(numbers, letters)

	rows = [rowtempl.format(number=number, letter=letter) for number, letter in lst]
	rows = "".join(rows)

	wholepage = bigtempl.format(rows=rows)

	print (wholepage)
	Helpers.db.connectDB()
	print("</body>")



def printEndSection():
	print("</html>")

printHeaders()
printStartSection()
printHomeBody()
printEndSection()
