#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa and prevent SQL injections
"""

import MySQLdb
import sys


if __name__ == "__main__":

    # connect to MYSQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # create a cursor object to execute queries
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY id ASC"
    name = (sys.argv[4],)

    # Execute the SQL query to fetch all the states in the database
    cursor.execute(query, name)

    #Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
