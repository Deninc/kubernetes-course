import os
import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI()
conn = None

@app.get("/")
def read_root():
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT count FROM counter WHERE id = 1")
            c = cur.fetchone()[0]
            c += 1
            cur.execute(f"UPDATE counter SET count = {c} WHERE id = 1")
    return f"pong {c}"

@app.get("/count")
def read_count():
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT count FROM counter WHERE id = 1")
            c = cur.fetchone()[0]
    return c

# readinessProbe check if Postgres is working
@app.get("/rediness")
def rediness():
    global conn
    try:
        if not conn:
            conn = psycopg2.connect(host="pg-svc", dbname="postgres", user="postgres", password=os.environ["POSTGRES_PASSWORD"])

        # https://www.psycopg.org/docs/usage.html#with-statement
        with conn:
            with conn.cursor() as cur:
                cur.execute("CREATE TABLE IF NOT EXISTS counter (id serial PRIMARY KEY, count integer);")
                cur.execute("INSERT INTO counter(id, count) VALUES (1, 0) ON CONFLICT (id) DO NOTHING;")
    except Exception as e:
        print(e)
        conn = None
        raise HTTPException(status_code=500, detail="Postgres server not ready")
    return
