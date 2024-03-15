#!/usr/bin/python3
"""Engine for db"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import base_model, city, state
import os

db = os.getenv("HBNB_TYPE_STORAGE")
user = os.getenv("HBNB_MYSQL_USER")
passwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")

engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@{host}:3306/{db}'
        )

session = sessionmaker(bind=engine)
session = session()


class DBStorage():
    __engine = None
    __session = None