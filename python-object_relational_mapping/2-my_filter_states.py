#!/usr/bin/python3
""" script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument. """


import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute SQL query using user input
    query = "SELECT * FROM states\
             WHERE name LIKE BINARY '{}'\
             ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)

    # Fetch all rows and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
