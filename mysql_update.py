from db_connection import get_connection

def update_user(user_id, new_email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))
    conn.commit()
    print(f"User {user_id} updated.")
    cursor.close()
    conn.close()

# Example
update_user(15, "alice@newdomain.com")
