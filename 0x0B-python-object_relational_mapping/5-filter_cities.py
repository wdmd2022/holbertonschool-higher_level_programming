#!/usr/bin/python3
"""this module contains a script that lists all cities from the table
hbtn_0e_0_usa using MySQLdb, sorted by cities.id (asc), and only using
execute() once. Takes 3 args: mysql username, mysql pass, db name"""

import MySQLdb
import sys

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    ORDER BY id;")
        records = cur.fetchall()
        for record in records:
            print(record)
        # Close cursor
        cur.close()
        # Close database
        db.close()
    except Exception:
        quit
