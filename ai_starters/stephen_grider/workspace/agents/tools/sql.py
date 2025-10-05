import sqlite3
from langchain.tools import Tool

import os
print("Connected to:", os.path.abspath("db.sqlite"))

conn = sqlite3.connect("db.sqlite")

def run_sqlite_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following error occured ; {str(err)}"

run_query_tool = Tool.from_function(
    name="run_sqllite_query",
    description="Run a sql query",
    func=run_sqlite_query
)


def list_tables():
    c = conn.cursor()
    c.execute("select name from sqlite_master where type='table';")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)