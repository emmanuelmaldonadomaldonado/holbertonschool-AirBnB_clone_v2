#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


from engine.file_storage import FileStorage
import os

storage = os.getenv("HBNB_TYPE_STORAGE")

if storage == "DBStorage":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
