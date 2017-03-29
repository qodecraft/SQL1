import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	c.execute("UPDATE inventory SET make = 'Shit' WHERE quantity = 40")

	c.execute("UPDATE inventory SET  quantity = 100 WHERE model = 'Ass'")

	c.execute("SELECT * FROM inventory")

	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1], r[2])


	c.execute("SELECT * FROM inventory WHERE make = 'Ford'")

	row = c.fetchall()

	print("___________")
	for r in row:
		print(r[0], r[1], r[2])

