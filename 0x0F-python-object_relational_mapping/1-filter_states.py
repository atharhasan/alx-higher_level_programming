#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    query = db.cursor()
    query.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id"
    )

    query_rows = query.fetchall()
    for row in query_rows:
        print(row)
    query.close()
    db.close()
