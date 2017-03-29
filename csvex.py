import sqlite3

import csv

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	employees = csv.reader(open("employees.csv", "rU"))

	c.execute("""CREATE TABLE employees
					(firstname TEXT, lastname TEXT)
					""")
	c.executemany("INSERT INTO employees(firstname, lastname) VALUES (?, ?)", employees)