import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	sql = {
			'average': "SELECT AVG(population) FROM population",
			'maximum': "SELECT MAX(population) FROM population",
			'minimum': "SELECT MIN(population) FROM population",
			'count': "SELECT COUNT(population) FROM population",
			'sum' : "SELECT SUM(population) FROM population"
		}	

	for keys, values in sql.items():
		c.execute(values)

		result = c.fetchone()

		print(keys + ":", result[0])