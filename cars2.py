import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	cars = [
		('Honda', 'Subra', 80),
		('Honda', 'Civic', 20),
		('Ford', 'Escort', 40),
		('Ford', 'Ass', 45),
		('Ford', 'Hay', 30)
	]

	c.executemany("""INSERT INTO inventory VALUES(?,?,?)""", cars)

	print("\nNew Data\n")

	c.execute("SELECT * FROM inventory")

	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1], r[2])



