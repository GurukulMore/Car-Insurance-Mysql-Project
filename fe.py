import tkinter as tk
import mysql.connector
import pandas as pd
import time
import schedule

def submit_data():
    policy_id = entry_policy_id.get()
    customer_name = entry_customer_name.get()
    car_details = entry_car_details.get()
    premium = entry_premium.get()

    insert_data(policy_id, customer_name, car_details, premium)

def delete_data():
    policy_id_to_delete = entry_delete_policy_id.get()
    try:
        cursor.execute("DELETE FROM insurance_data WHERE policy_id = %s", (policy_id_to_delete,))
        conn.commit()
        result_label.config(text="Record deleted successfully!", fg="green")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        result_label.config(text="Error deleting record", fg="red")

def insert_data(policy_id, customer_name, car_details, premium):
    try:
        cursor.execute("INSERT INTO insurance_data (policy_id, customer_name, car_details, premium) VALUES (%s, %s, %s, %s)",
                       (policy_id, customer_name, car_details, premium))
        conn.commit()

        # Save data to Excel file
        save_to_excel()

        result_label.config(text="Data inserted successfully!", fg="green")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        result_label.config(text="Error inserting data", fg="red")

def save_to_excel():
    cursor.execute("SELECT * FROM insurance_data")
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=['ID', 'Policy ID', 'Customer Name', 'Car Details', 'Premium'])
    df.to_excel('insurance_data.xlsx', index=False)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vaishali.123",
    database="car_insurance"
)



cursor = conn.cursor()

root = tk.Tk()
root.title("Car Insurance Data Entry")

# Create a frame for better organization
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label_policy_id = tk.Label(frame, text="Policy ID")
label_customer_name = tk.Label(frame, text="Customer Name")
label_car_details = tk.Label(frame, text="Car Details")
label_premium = tk.Label(frame, text="Premium")
label_delete_policy_id = tk.Label(frame, text="Policy ID to Delete")
entry_delete_policy_id = tk.Entry(frame)


entry_policy_id = tk.Entry(frame)
entry_customer_name = tk.Entry(frame)
entry_car_details = tk.Entry(frame)
entry_premium = tk.Entry(frame)

submit_button = tk.Button(frame, text="Submit", command=submit_data)

# Add some padding and change background color
frame.configure(bg='#f0f0f0')
submit_button.configure(bg='#4caf50', fg='white', font=('Arial', 12))

delete_button = tk.Button(frame, text="Delete", command=delete_data)
delete_button.configure(bg='#f44336', fg='white', font=('Arial', 12))
delete_button.grid(row=7, columnspan=2, pady=(10, 0))


label_policy_id.grid(row=0, column=0, pady=(0, 5))
entry_policy_id.grid(row=0, column=1, pady=(0, 5))
label_customer_name.grid(row=1, column=0, pady=(0, 5))
entry_customer_name.grid(row=1, column=1, pady=(0, 5))
label_car_details.grid(row=2, column=0, pady=(0, 5))
entry_car_details.grid(row=2, column=1, pady=(0, 5))
label_premium.grid(row=3, column=0, pady=(0, 5))
entry_premium.grid(row=3, column=1, pady=(0, 5))
submit_button.grid(row=4, columnspan=2, pady=(10, 0))

# Add a result label
result_label = tk.Label(frame, text="", font=('Arial', 12, 'bold'))
result_label.grid(row=5, columnspan=2)
label_delete_policy_id.grid(row=6, column=0, pady=(0, 5))
entry_delete_policy_id.grid(row=6, column=1, pady=(0, 5))


# Start the GUI event loop
root.mainloop()

cursor.close()
conn.close()