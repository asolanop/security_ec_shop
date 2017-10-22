#!/usr/local/bin/python3
import os

print("Content-Type: text/html\r\n\r\n")
print()
print(os.getenv("HTTP_REFERER"))