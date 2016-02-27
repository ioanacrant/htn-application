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

#def populate_users(db="users.db"):

def isolate_user_info():
    JSON_FILE = requests.get("https://htn-interviews.firebaseio.com/users.json").json()
    userarray = []
    for user in JSON_FILE:
        print(user)
        userarray.append(user["name"], user["picture"],user["company"], user["email"], user["phone"],
                        user["country"], user["latitude"], user["longitude"])
    return userarray

#isolate_user_info()
