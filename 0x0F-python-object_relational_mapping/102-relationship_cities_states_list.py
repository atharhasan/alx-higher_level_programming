#!/usr/bin/python3
''' a script that lists all City objects from the database hbtn_0e_101_usa '''


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           username, password, dbname),
                           pool_pre_ping=True)

    session = Session(bind=engine)
    query = session.query(City).order_by(City.id).all()

    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
