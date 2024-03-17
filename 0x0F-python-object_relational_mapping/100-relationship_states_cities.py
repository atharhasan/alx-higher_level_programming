#!/usr/bin/python3
''' a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa '''


import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           username, password, dbname),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state_to_add = State(name='California')
    city_to_add = City(name='San Francisco')
    city_to_add.state = state_to_add

    session.add(city_to_add)
    session.commit()
    session.close()
