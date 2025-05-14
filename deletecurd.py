from db_connection import get_connection

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    print(f"User {user_id} deleted.")
    cursor.close()
    conn.close()

# Example
delete_user(15)

