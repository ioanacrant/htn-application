import sqlite3
import json
import requests

def create_db(db="users.db"):
    connection = sqlite3.connect(db)
    c = connection.cursor()
    c.execute('''CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    picture TEXT,
                    company TEXT,
                    email TEXT,
                    phone TEXT,
                    latitude NUMBER,
                    longitude NUMBER)''')

    c.execute('''CREATE TABLE skills (
                    skill_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    name TEXT,
                    rating NUMBER,
                    FOREIGN KEY (user_id) REFERENCES users(id))''')

def populate_users(db="users.db"):
    connection = sqlite3.connect(db)
    c = connection.cursor()

    userinfo = isolate_user_info()
    for userkeys in userinfo:
        c.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?)", userkeys)
    connection.commit()

def isolate_user_info():
    JSON_FILE = requests.get("https://htn-interviews.firebaseio.com/users.json").json()
    userarray = []
    for i in range(len(JSON_FILE)):
        user = JSON_FILE[i]
        userarray.append([i+1,user["name"], user["picture"],user["company"], user["email"], user["phone"],
                        user["latitude"], user["longitude"]])
    return userarray
