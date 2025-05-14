import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abhi",  # Replace with your actual password
        database="testdb"         # Replace with your database name
    )
