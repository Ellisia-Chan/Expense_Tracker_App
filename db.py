import sqlite3
import os

# Get the directory where the py script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the SQLite database file
db_file = os.path.join(script_dir, "finance.db")

def create_database(): 
    # Check if the database file already exists
    if not os.path.exists(db_file):
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(db_file)

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Create expenses table with date as the first column
        cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                            date DATE,
                            id INTEGER PRIMARY KEY,
                            category TEXT,
                            name TEXT,
                            amount REAL
                        )''')
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        # For Debugging
        # print("Database created successfully at:", db_file)
    # else:
        # print("Database already exists at:", db_file)
        
# Get all Data from the table
def load_entries(current_date):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries WHERE date = ?", (current_date,))
    entries = cursor.fetchall()
    conn.close()

    if entries:
        return entries
    
# Get Total Balance 
def total_amount():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM entries WHERE category = 'Income'")
    income = cursor.fetchone()  # Fetch the sum of amounts
    
    income_result = 0
    if income[0] is not None:
        income_result = income[0]
    else:
        income_result = 0
        

    cursor.execute("SELECT SUM(amount) FROM entries WHERE category = 'Expense'")
    expense = cursor.fetchone() # Fetch the sum of amounts
    
    expense_result = 0
    if expense[0] is not None:
        expense_result = expense[0]
    else:
        expense_result = 0

    total_balance = income_result - expense_result

    conn.close()
    if total_balance:
        return total_balance


# Add Data
def add_data_to_table(date, category, name, amount):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    if category == "Expense":
        cursor.execute("INSERT INTO entries (date, category, name, amount) VALUES (?, ?, ?, ?)", (date, category, name, amount))
        conn.commit()

    if category == "Income":
        cursor.execute("INSERT INTO entries (date, category, name, amount) VALUES (?, ?, ?, ?)", (date, category, name, amount))
        conn.commit()
        
    # Close connection
    conn.close()
    
# Update a single row of Data  
def update_data_in_table(id, name, category, amount, date):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM entries WHERE date=? AND id=?", (date, id))
    fetched_id = cursor.fetchone()
    
    if fetched_id is not None and int(id) == fetched_id[0]:
        cursor.execute("UPDATE entries SET name=? WHERE id=?", (name, id))
        cursor.execute("UPDATE entries SET category=? WHERE id=?", (category, id))
        cursor.execute("UPDATE entries SET amount=? WHERE id=?", (amount, id))
        conn.commit()
        conn.close()
    else:
        conn.close()
        return True
    
# Delete a single row of Data
def delete_data_in_table(id, date):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM entries WHERE id=? AND date=?", (id, date))
    fetched_id = cursor.fetchone()
    
    if fetched_id is not None and int(id) == fetched_id[0]:
        cursor.execute("DELETE FROM entries WHERE id=? AND date=?", (id, date))
        conn.commit()
        conn.close()
    else:
        conn.close()
        return True
       
# Delete All data Entries    
def delete_all_data_in_table():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM entries")
    conn.commit()
    conn.close()
    
# Delete All data Entries    
def delete_all_data_in_table():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM entries")
    conn.commit()
    conn.close()
    
# Get total income/expenses in current month and year
def get_income_expense_total(month, year):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Construct the query to get income and expenses for the specified month and year
    cursor.execute("SELECT SUM(amount) FROM entries WHERE SUBSTR(date, 1, INSTR(date, ' ') - 1) = ? AND SUBSTR(date, -4) = ? AND category = 'Income'", (month, year))
    total_income = cursor.fetchone()[0]
    
    cursor.execute("SELECT SUM(amount) FROM entries WHERE SUBSTR(date, 1, INSTR(date, ' ') - 1) = ? AND SUBSTR(date, -4) = ? AND category = 'Expense'", (month, year))
    total_expense = cursor.fetchone()[0]
    
    conn.close()
    
    if total_income is None:
        total_income = 0
    if total_expense is None:
        total_expense = 0
    
    return total_income, total_expense

# Get income list in current month and year
def get_income_list(month, year):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries WHERE SUBSTR(date, 1, INSTR(date, ' ') - 1) = ? AND SUBSTR(date, -4) = ? AND category = 'Income' ", (month, year))
    
    entries = cursor.fetchall()
    if entries:
        conn.close()
        return entries
    conn.close()

# Get expense list in current month and year
def get_expense_list(month, year):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries WHERE SUBSTR(date, 1, INSTR(date, ' ') - 1) = ? AND SUBSTR(date, -4) = ? AND category = 'Expense' ", (month, year))
    
    entries = cursor.fetchall()
    if entries:
        conn.close()
        return entries
    conn.close()


def filter_category(date, filter_num):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    if filter_num == 1:
        cursor.execute("SELECT * FROM entries WHERE category = 'Expense' AND date = ?", (date,))
        entries = cursor.fetchall()
        conn.close()
        return entries  
    elif filter_num == 2:
        cursor.execute("SELECT * FROM entries WHERE category = 'Income' AND date = ?", (date,))
        entries = cursor.fetchall()
        conn.close()
        return entries
    conn.close()