import sqlite3
with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("INSERT INTO population VALUES('Los Angeles', 'LA', 85000)")
	