import sqlite3

# Connect to the database
conn = sqlite3.connect('beermeal.db')
c = conn.cursor()

# Delete all rows from the table
c.execute('DELETE FROM ShopProducts')

# Reset the AUTOINCREMENT counter to 1
c.execute("DELETE FROM sqlite_sequence WHERE name='ShopProducts'")

# Commit the changes and close the connection
conn.commit()
conn.close()