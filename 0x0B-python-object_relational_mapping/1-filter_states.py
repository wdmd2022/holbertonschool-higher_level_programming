#!/usr/bin/python3
"""this module contains a function that uses MySQLdb"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    records = cur.fetchall()
    for record in records:
        print(record)
