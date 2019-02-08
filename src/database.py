# -*- coding: utf-8 -*-
import sys
import io
import traceback
from pathlib import Path
from peewee import *
from playhouse.postgres_ext import *
from playhouse.migrage import *
import arrow

sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

db = PostgresqlExtDatabase(
    database = '',
    user = '',
    password = '',
    host = 'localhost',
    port = 5432,
    register_hstore = False
db.connect()

migrator = PostgresqlMigrator(db)

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name       = CharField()
    email      = TextField()
    tel        = CharField()
    birthday   = DateField()
    created_at = DateTimeField(default=arrow.utcnow().shift(hours=9).format())
    updated_at = DateTimeField(default=arrow.utcnow().shift(hours=9).format())
    
if __name__ == '__main__':
    try:
        if not Person.table_exists():
            db.create_tables([Person], safe=True)

        with db.transaction():
            Person.insert_many([
                {'name': 'aaa', 'email': 'aaa@aaa.com', 'birthday': arrow.get('2018/1/1').format()},
                {'name': 'bbb', 'email': 'bbb@bbb.com', 'birthday': arrow.get('2018/1/2').format()},
            ]).execute()

    except Exception as e:
        db.rollback()
        traceback.print_exc()
        raise
    finally:
        db.close()
