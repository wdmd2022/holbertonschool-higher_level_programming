#!/usr/bin/python3
"""this module contains a script that lists all cities from a state in
hbtn_0e_0_usa using MySQLdb, sorted by cities.id (asc), safe from injection,
and only using execute() once. Takes 4 args: mysql username, mysql pass, db
name, state"""

import MySQLdb
import sys

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities LEFT JOIN states ON BINARY\
                    cities.state_id = states.id WHERE states.id = (SELECT\
                    id FROM states WHERE name = %s) ORDER BY cities.id",
                    (sys.argv[4],))
        rows = cur.fetchall()
        if len(rows) <= 0:
            print("")
            quit
        for row in rows:
            if row == rows[-1]:
                print(row[0])
            else:
                print("{}".format(row[0]), end=", ")
        # Close cursor
        cur.close()
        # Close database
        db.close()
    except Exception:
        quit
