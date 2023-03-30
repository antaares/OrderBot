import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            Name varchar(255),
            language varchar(5)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    

    def add_user(self, id, name, language):
        sql = "INSERT OR IGNORE INTO Users (id, Name, language) VALUES (?, ?, ?)"
        self.execute(sql, parameters=(id, name, language), commit=True)
    
    def select_lang(self, id):
        sql = "SELECT language FROM Users WHERE id = ?"
        return self.execute(sql, parameters=(id,), fetchone=True)[0]

    def update_lang(self, id, language):
        sql = "UPDATE Users SET language = ? WHERE id = ?"
        self.execute(sql, parameters=(language, id), commit=True)