#!/usr/local/bin/python3
import os
import pymysql.cursors

print("Content-Type: text/html")
print("HTTP_COOKIE: amor=Mich")
print("HTTP_COOKIE: session_id=A81JS91")
print()
print ("""\
<html>
<body style="background:PINK" >
<h2 style="margin-left:48%;color:WHITE">Hello Amor <3</h2>
</body>
</html>
""")
print(os.getenv("QUERY_STRING"))
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='ecstore',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()