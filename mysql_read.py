from db_connection import get_connection

def read_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    cursor.close()
    conn.close()

# Example
read_users()
