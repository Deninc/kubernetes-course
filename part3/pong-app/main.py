import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

conn = psycopg2.connect(host="pg-svc", dbname="postgres", user="postgres", password=os.environ["POSTGRES_PASSWORD"])

# https://www.psycopg.org/docs/usage.html#with-statement
with conn:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS counter (id serial PRIMARY KEY, count integer);")
        cur.execute("INSERT INTO counter(id, count) VALUES (1, 0) ON CONFLICT (id) DO NOTHING;")

@app.get("/pingpong")
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
