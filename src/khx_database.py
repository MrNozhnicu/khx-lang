#!/usr/bin/env python3
"""
KHX Database Module - SQL and NoSQL Support
"""

import sqlite3
import json
from typing import Any, Dict, List


class KHXDatabase:
    """Database wrapper for KHX"""
    
    def __init__(self, db_type="sqlite", connection_string="memory"):
        self.db_type = db_type
        self.connection_string = connection_string
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """Connect to database"""
        if self.db_type == "sqlite":
            if self.connection_string == "memory":
                self.connection = sqlite3.connect(":memory:")
            else:
                self.connection = sqlite3.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            print(f"[DB] Connected to SQLite: {self.connection_string}")
            return True
        return False
    
    def query(self, sql, params=None):
        """Execute SELECT query"""
        if not self.cursor:
            return []
        
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            
            columns = [desc[0] for desc in self.cursor.description]
            results = []
            for row in self.cursor.fetchall():
                results.append(dict(zip(columns, row)))
            return results
        except Exception as e:
            print(f"[DB] Query error: {e}")
            return []
    
    def execute(self, sql, params=None):
        """Execute INSERT/UPDATE/DELETE"""
        if not self.cursor:
            return False
        
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"[DB] Execute error: {e}")
            return False
    
    def create_table(self, table_name, columns):
        """Create table"""
        cols = ", ".join([f"{name} {type_}" for name, type_ in columns.items()])
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})"
        return self.execute(sql)
    
    def insert(self, table_name, data):
        """Insert record"""
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        return self.execute(sql, tuple(data.values()))
    
    def update(self, table_name, data, where):
        """Update records"""
        set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
        return self.execute(sql, tuple(data.values()))
    
    def delete(self, table_name, where):
        """Delete records"""
        sql = f"DELETE FROM {table_name} WHERE {where}"
        return self.execute(sql)
    
    def close(self):
        """Close connection"""
        if self.connection:
            self.connection.close()
            print("[DB] Connection closed")


# Global database registry
_databases = {}
_db_counter = 0


def connect_database(db_type="sqlite", connection_string="memory"):
    """Connect to database"""
    global _db_counter
    db = KHXDatabase(db_type, connection_string)
    db.connect()
    db_id = f"db_{_db_counter}"
    _databases[db_id] = db
    _db_counter += 1
    return db_id


def get_database(db_id):
    """Get database by ID"""
    return _databases.get(db_id)
