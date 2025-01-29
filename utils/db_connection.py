import pyodbc

# Define connection details
server = '10.50.31.79'
database = 'RoutePermit_Dev'
username = 'Ameer_Hamza'
password = 'Test@1234'

# Establish connection
connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

print("Connection established!")

# Create a cursor
cursor = connection.cursor()

# Example query
query = "SELECT * FROM Users where UserName = '31101-4549242-3'"

# Execute the query
cursor.execute(query)

# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
