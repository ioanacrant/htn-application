import sqlite3
import json

#JSON_FILE =
DB_FILE = "users.db"

#traffic = json.load(open(JSON_FILE))
connection = sqlite3.connect(DB_FILE)


c = connection.cursor()
c.execute('''CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                picture TEXT,
                company TEXT,
                email TEXT,
                phone TEXT,
                country TEXT,
                latitude NUMBER,
                longitude NUMBER)''')

c.execute('''CREATE TABLE skills (
                skill_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                name TEXT,
                rating NUMBER,
                FOREIGN KEY (user_id) REFERENCES users(id))''')
