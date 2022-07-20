import sqlite3

with sqlite3.connect("netflix.db") as connection:
    connection.execute("""
    SELECT * FROM 'netflix'
    """)
    connection_query = connection.fetchall()
    result = connection_query

    print(result)