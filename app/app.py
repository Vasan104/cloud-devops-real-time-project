from flask import Flask, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="devops-rds.caz0ecyo642l.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Vasan10401",
    database="devopsdb"
)

@app.route("/")
def home():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
