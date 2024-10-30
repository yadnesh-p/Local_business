import sqlite3
from flask import g

def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database = sqlite3.connect('app/database.db')
    return db

#Changed for local setup
#def close_db():
def close_db(e=None):
    db = g.pop('_database',None)
    if db is not None:
        db.close()