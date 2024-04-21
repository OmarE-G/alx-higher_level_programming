#!/usr/bin/python3
"""Base State Class"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(usr, pwd, db))

    conn = engine.connect()
    Sess = sessionmaker(bind=engine)
    sess = Sess()

    for row in sess.query(State, City).filter(
        State.id == City.state_id
    ).all():
        print(f"{row.State.name}: ({row.City.id}) {row.City.name}")
