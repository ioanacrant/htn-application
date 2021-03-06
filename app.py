import sqlite3
import json
from flask import Flask, request, g
app = Flask(__name__)

@app.route("/")
def hello():
    return "hey htn"

@app.route("/users", methods=["GET"])
def show_users():
    users = query_db("SELECT * FROM users")
    for user in users:
        user_id = user["id"]
        skills = query_db("SELECT * FROM skills WHERE user_id=?",[user_id], 2)
        user["skills"]=skills

    return json.dumps(users)

@app.route("/users/<int:user_id>", methods=["GET", "PUT"])
def show_user(user_id):
    if request.method == 'GET':
        user = query_db("SELECT * FROM users WHERE id=?", [user_id])[0]
        skills = query_db("SELECT * FROM skills WHERE user_id=?",[user_id], 2)
        user["skills"]=skills
        return json.dumps(user)

    else:
        req = request.get_json()
        user = query_db("SELECT * FROM users WHERE id=?", [user_id])[0]
        for key in req:
            if key in ["name", "picture", "company", "email", "phone", "latitude", "longitude"]:
                user[key]= req[key]
        g.db.execute("UPDATE users SET name=?, picture=?, company=?, email=?, phone=?, latitude=?, longitude=? WHERE id=?",
                    [user["name"], user["picture"], user["company"], user["email"], user["phone"], user["latitude"], user["longitude"], user_id])
        newuser = query_db("SELECT * FROM users WHERE id=?", [user_id])[0]
        skills = query_db("SELECT * FROM skills WHERE user_id=?",[user_id], 2)
        newuser["skills"]=skills
        return json.dumps(newuser)

@app.before_request             #found on sql site
def before_request():
    g.db = db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

def db(database="users.db"):
    return sqlite3.connect(database)

def query_db(query, args=(), startfrom=0):
    c = g.db.execute(query, args)
    rows = [dict((c.description[i][0], value) \
               for i, value in enumerate(row) if i>=startfrom) for row in c.fetchall()]
    return rows


if __name__ == '__main__':
    app.run()
