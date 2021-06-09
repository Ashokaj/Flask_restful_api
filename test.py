import sqlite3

connection = sqlite3.connect('data.db')
Cursor = connection.cursor()

create_table = "CREATE TABLE users (id int,username text,password text)"
Cursor.execute(create_table)

user = [
    (1,'ashok','asdf'),(2,'jana','lkjh'),(3,'aj','xyz')
]
insert_query = "INSERT INTO users VALUES(?,?,?)"
Cursor.executemany(insert_query,user)

select_query = "select * from users"
for row in Cursor.execute(select_query):
    print(row)
connection.commit()
connection.close()

