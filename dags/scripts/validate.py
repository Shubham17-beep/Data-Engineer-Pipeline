import sqlite3
import pandas as pd

# Create a connection to the database
conn = sqlite3.connect('sentiment.db')

# Create a SQL query to select all data from the table
query = "SELECT * FROM SentimentScores"

# Use pandas to read the SQL query into a DataFrame
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()