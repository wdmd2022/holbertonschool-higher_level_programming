#!/usr/bin/python3
"""this module contains a script that prints states from the table
hbtn_0e_0_usa where the name value matches the last argument given"""

import MySQLdb
import sys

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        searchterm = sys.argv[4].split()
        cur.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER\
            BY id;".format(searchterm[0]))
        records = cur.fetchall()
        for record in records:
            print(record)
        # Close cursor
        cur.close()
        # Close database
        db.close()
    except Exception:
        quit
