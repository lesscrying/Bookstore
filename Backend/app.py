from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Flask API is running!"

@app.route('/db')
def db_connect():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db",  # Имeто на услугата от Docker Compose
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        return f"Connected to DB: {db_version}"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
