from db_connection import get_connection

def create_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("User created.")
    cursor.close()
    conn.close()

# Example
create_user("Alice", "alice@example.com")
