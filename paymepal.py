from flask import Flask, render_template, request,session
from sqlalchemy import create_engine


app = Flask(__name__)
app.config["SECRET_KEY"] = "very secret stuff"
engine = create_engine("sqlite:///paymepal.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["user"]
    password = request.form["password"]
    with engine.connect() as connection:
        query = "SELECT USERNAME, PASSWORD FROM USERS"
        
        result = connection.execute(query)
        for row in result:
            session["username"] = username
            session["user_id"] = rows[0][0]
            if username == row[0] and password == row[1]:
                return render_template("private.html")
            else:
                return render_template("unauthorized.html"), 403


app.run(debug=True, port=8080)