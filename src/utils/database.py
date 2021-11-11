import sqlite3
import asyncio

async def create_wiki_table():
    conn = sqlite3.connect('src/data/wiki.db', isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS wiki (name text, owner_id text, description text)")
    conn.commit()
    conn.close()
    
async def insert_wiki_data(name: str, owner_id: str, description: str):
    name = name.replace(" ", "_")
    conn = sqlite3.connect('src/data/wiki.db', isolation_level=None)
    c = conn.cursor()
    c.execute("INSERT INTO wiki VALUES (?, ?, ?)", (name, owner_id, description))
    conn.commit()
    conn.close()
    
async def get_wiki_data(name: str):
    conn = sqlite3.connect('src/data/wiki.db', isolation_level=None)
    c = conn.cursor()
    c.execute("SELECT * FROM wiki WHERE name=?", (name,))
    data = c.fetchall()
    return data

async def get_all_wiki_data():
    conn = sqlite3.connect('src/data/wiki.db', isolation_level=None)
    c = conn.cursor()
    c.execute("SELECT * FROM wiki")
    return c.fetchall()

async def edit_wiki_data(description: str):
    conn = sqlite3.connect('src/data/wiki.db', isolation_level=None)
    c = conn.cursor()
    c.execute("UPDATE wiki SET description = ?", (description,))
    conn.commit()
    conn.close()