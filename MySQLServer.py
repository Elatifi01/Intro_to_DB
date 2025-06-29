import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (replace with your own credentials)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',          # replace if your username is different
        password='yourpassword'  # replace with your real password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
