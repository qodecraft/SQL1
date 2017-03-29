import sqlite3

conn = sqlite3.connect("cars.db")

c = conn.cursor()

c.execute("""CREATE TABLE inventory
				(make TEXT, model TEXT, quantity INT)
				""")

c.close()

