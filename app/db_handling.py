import os
import sqlite3 as sql
from .user import User
from typing import List

DB_FILE = "app/data/databse.db"
CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    user_name text,
    password text,
    date text
);
"""

class Database:
    def __init__(self) -> None:
        conn = sql.connect(DB_FILE)
        cursor = conn.cursor()
        try:
            cursor.execute(CREATE_TABLE_USER)
            
            # Close resources.
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print(f'[!] Unable to open database.')
        
    def add_user(self, user: User) -> None:
        query = f"""INSERT INTO users VALUES(?, ?, ?)"""
        try:
            conn = sql.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(query, (user.name, user.password, user.registration))
            
            # Close all resources.
            conn.commit()
            cursor.close()
            conn.close()
            
        except (Exception, sql.Error) as e:
            print(f"[!] {e}")
            
    def get_user(self, user_name: str, password: str) -> dict:
        all_users = {}
        query = f"SELECT * FROM users WHERE user_name = '{user_name}' AND password = '{password}'"
        
        try:
            conn = sql.connect(DB_FILE)
            cursor = conn.cursor()
            
            cursor.execute(query)
            for row in cursor.fetchall():
                all_users.update({row[0]: row[1:]})

            cursor.close()
            conn.close()
            return all_users
        
        except (Exception, sql.Error) as e:
            print(f"[!] {e}")
            return {}
            
DB = Database()