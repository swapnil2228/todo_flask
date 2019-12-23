import os
import sqlite3
import pandas as pd


# Create a database
conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def sql_edit_insert(query,var):
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()
    conn.close()

def sql_delete(query,var):
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()
    conn.close()

def sql_query2(query,var):
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
