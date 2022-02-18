import sqlite3

conn=sqlite3.connect('appusers.db')
c=conn.cursor()
c.execute("DROP TABLE users_3")
c.execute(""" CREATE TABLE IF NOT EXISTS users_3(
                first text,
                last text,
                amount integer
                )""")
conn.commit

def inset_user(table,user):
    with conn:
        c.execute(f"INSERT into {table} VALUES (:first,:last,:amount)",{'first' : user.first,'last' : user.last,'amount' : user.amount})

def get_user_by_name(table,first):
        c.execute(f"SELECT * FROM {table} WHERE first=:first",{'first':first})
        fetchall()

def update_amount(table,user,amount):
    with conn:
        c.execute(f"""UPDATE {table} SET amount=:amount
                    WHERE first=:first AND last=:last""",
                  {'first':user.first,'last':user.last,'amount':amount))


def remove_user(table,user):
    with conn:
        c.execute(f"DELETE from {table} WHERE first=:first AND last=:last",
                  {'first':user.first,'last':user.last})
