#!/usr/bin/python3
"""lists all states from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    state_name = argv[4]


    sql_query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    num_rows = cur.execute(sql_query, (state_name,))
    
    for i in range(num_rows):
        print(cur.fetchone())

    cur.close()
    db.close()
