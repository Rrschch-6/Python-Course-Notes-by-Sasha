import sqlite3

conn=sqlite3.connect('appusers.db')
#in memmory database: conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS users_1(
                first text,
                last text,
                amount integer
                )""")
conn.commit

c.execute("INSERT into users_1 VALUES ('Sasha','Behrouzi',1000)")

c.execute("SELECT * FROM users_1 WHERE first='Sasha'")
print(c.fetchone())
#print(fetchall())
#print(c.fetchmaby(5))