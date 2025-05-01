import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Step 2: Create the 'sales' table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Step 3: Insert sample data
sample_data = [
    ('Apple', 10, 2.0),
    ('Banana', 5, 1.0),
    ('Orange', 8, 1.5),
    ('Apple', 7, 2.0),
    ('Banana', 3, 1.0),
    ('Orange', 4, 1.5),
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit()

# Step 4: Run SQL query for sales summary
query = '''
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
'''
df = pd.read_sql_query(query, conn)

# Step 5: Print the DataFrame
print("Sales Summary:")
print(df)

# Step 6: Plot a simple bar chart of revenue per product
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close the connection
conn.close()
