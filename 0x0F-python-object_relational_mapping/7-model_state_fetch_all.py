#!/usr/bin/python3
"""Base State Class"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main___':
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(usr, pwd, db), echo=True)

    conn = engine.connect()
    Sess = sessionmaker(bind=engine)
    sess = Sess()
    
    for row in sess.query(State).order_by(State.id):
        print(row[0] + ': ' + row[1])

