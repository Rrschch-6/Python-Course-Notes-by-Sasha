class user:
    def __init__(self,first,last,amount):
        self.first=first
        self.last=last
        self.amount=amount

user1=user('Sasha','Behrouzi',1000)
user2=user('Peter','Parker',2000)
user3=user('steve','banon',3000)
user4=user('bruce','wane',4000)


import sqlite3

conn=sqlite3.connect('appusers.db')
#in memmory database: conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS users_2(
                first text,
                last text,
                amount integer
                )""")
conn.commit

#method 1
#c.execute(f"INSERT into users_2 VALUES ('{user2.first}','{user2.last}',{user2.amount})")


#method 2
#c.execute("INSERT into users_2 VALUES (?,?,?)",(user3.first,user3.last,user3.amount))

#method 3

c.execute("INSERT into users_2 VALUES (:first,:last,:amount)",{'first' : user4.first,'last' : user4.last,'amount' : user4.amount})
c.execute("SELECT * FROM users_2")
print(c.fetchall())