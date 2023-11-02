import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vaishali.123",
    database="car_insurance"
)

cursor = conn.cursor()

# Create a table to store insurance data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS insurance_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        policy_id VARCHAR(255) NOT NULL,
        customer_name VARCHAR(255) NOT NULL,
        car_details VARCHAR(255) NOT NULL,
        premium DECIMAL(10, 2) NOT NULL
    )
""")

cursor.close()
conn.close()