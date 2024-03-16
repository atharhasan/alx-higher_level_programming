#!/usr/bin/python3
"""Lists cities"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name\
        FROM cities INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s",
        [argv[4]],
    )
    query_rows = cur.fetchall()

    list = []
    for i in query_rows:
        list.append(i[1])
        print(", ".join(list))

    cur.close()
    conn.close()
