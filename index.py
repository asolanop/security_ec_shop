#!/usr/bin/python3

import Helpers.db

# Print necessary headers.
print("Content-Type: text/html")
print()

print("Index Page")
Helpers.db.connectDB()
