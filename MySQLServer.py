import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (adjust user and password as needed)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Babatunde"  
        )
        cursor = conn.cursor()

        # Try to create database (IF NOT EXISTS)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up resources
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()