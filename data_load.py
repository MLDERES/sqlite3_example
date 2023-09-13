import sqlite3
from pathlib import Path

# Define the path to the data
data_folder = Path("d:\\projects\\sqlite3_example\\data")
# Set the database filename
db_filename = data_folder / "drinks.db"

# Set the data filename
data_filename = data_folder / "drinks.csv"

# Create the database
#   Connect to the database
conn = sqlite3.connect(db_filename)
#   Create a cursor object
cur = conn.cursor()
#   Drop the table if it exists
cur.execute("DROP TABLE IF EXISTS drinks")
#   Create the table
cur.execute("CREATE TABLE drinks (" +
            "country TEXT,beer_servings REAL,spirit_servings REAL,wine_servings REAL,total_litres_of_pure_alcohol REAL)")

# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cur.fetchall()
# print(tables)

# Load data from data file
#   Load data from csv file
for row in open(data_filename):
    #   Skip the header row
    if row.startswith('country'):
        continue
    #   Insert the data into the table
    cur.execute("INSERT INTO drinks VALUES (?,?,?,?,?)", row.split(','))
#   Commit the changes
    conn.commit()

# Select all rows from the table
cur.execute("SELECT * FROM drinks")
# Print the result
print(cur.fetchall())
# Close the cursor
cur.close()
# Close the connection
conn.close()

