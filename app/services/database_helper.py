from datetime import date, datetime
from pydal import DAL, Field
from setup import config

def define_database():
    db = DAL(config.CONNECTION_STRING, folder='dbs', auto_import=True,migrate_enabled=False, fake_migrate=False)
    db.define_table('users',
                Field('id', 'integer'), 
                Field('name', required=True),
                Field('password', required=True), 
                Field('email', required=True),
                Field('created_at', required=True),
                Field('updated_at', required=False),
                Field('active',bool = True),
                primarykey = ['id']
                )
    return db