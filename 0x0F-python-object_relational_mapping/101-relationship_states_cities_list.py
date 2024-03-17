#!/usr/bin/python3
''' a script that lists all State objects
and corresponding City objects
contained in the database hbtn_0e_101_usa '''


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

    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    query = session.query(State).order_by(State.id).all()

    for st in query:
        print("{}: {}".format(st.id, st.name))
        for cit in st.cities:
            print("\t{}: {}".format(cit.id, cit.name))

    session.close()
