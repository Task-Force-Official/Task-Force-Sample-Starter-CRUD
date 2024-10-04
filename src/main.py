import sqlite3

# Connect to the SQLite database (it will create a file called recipes.db)
conn = sqlite3.connect('/Users/aarush/Documents/Coding/TASK-FORCE-TRYOUTS-STARTER/src/recipes.db')

# Create a cursor object
cur = conn.cursor()

# Create the recipes table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS recipes (
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

