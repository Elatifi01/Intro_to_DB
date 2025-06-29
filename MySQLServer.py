import mysql.connector

try:
    # Connect to MySQL server (update user/password if needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword'  # replace with your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
