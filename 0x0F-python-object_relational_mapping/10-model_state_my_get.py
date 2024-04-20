#!/usr/bin/python3
"""Base State Class"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(usr, pwd, db))

    conn = engine.connect()
    Sess = sessionmaker(bind=engine)
    sess = Sess()

    row = sess.query(State).filter(State.name == state_name).first()
    if(row is None):
        print("Nothing")
    else:
        print(row.id)
