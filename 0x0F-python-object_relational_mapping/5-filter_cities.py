#!/usr/bin/python3
"""mysql state from dayae"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    dbnames = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    query = dbnames.cursor()
    query.execute(
        "SELECT cities.id, cities.name\
                  FROM cities INNER JOIN states ON cities.state_id=states.id\
                  WHERE states.name = %s",
        [argv[4]],
    )

    test = []
    for i in query.fetchall():
        test.append(i[1])
    print(", ".join(test))

    query.close()
    dbnames.close()
