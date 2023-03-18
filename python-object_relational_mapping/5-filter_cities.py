#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Create a cursor object to execute queries
    cursor = db.cursor()

    query = "SELECT cities.name\
             FROM cities\
             INNER JOIN states\
             ON cities.state_id = states.id\
             WHERE BINARY states.name LIKE %s\
             ORDER BY cities.id ASC"
    name = (sys.argv[4],)

    # Execute SQL query to fetch all cities of that states
    cursor.execute(query, name)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    first = True
    for row in rows:
        if first:
            first = False
        else:
            print(",", end=" ")
        for col in row:
            print("%s" % col, end="")
    print()

    # Close cursor and db connection
    cursor.close()
    db.close()
