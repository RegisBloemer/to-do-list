import sqlite3

data_base = sqlite3.connect('data_base')

cursor = data_base.cursor()

cursor.execute("CREATE TABLE List (name tinytext,list_id integer PRIMARY KEY);")

cursor.execute("CREATE TABLE Task (description text,list_id integer,task_id integer PRIMARY KEY,FOREIGN KEY(list_id) REFERENCES List (list_id));")

data_base.commit()

