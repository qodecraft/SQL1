import sqlite3

conn = sqlite3.connect("new.db")

c = conn.cursor()

c.execute("""INSERT INTO population VALUES
			('New York City', 'NY', 8400000)
	""")


c.execute("""INSERT INTO population VALUES
			('San Francisco', 'CA', 8000000)
	""")

conn.commit()

conn.close()