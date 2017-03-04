from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime


db = SqliteExtDatabase('example.db')


class BaseModel(Model):
    class Meta:
        database = db 

class Todo(BaseModel):
    id = IntField()
    content = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)
    deadlineDate = DateTimeField()
    is_done = BooleanField(default=False)
    tags = TextField()
    
class Vocab(BaseModel):
    id = IntField()
    content = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)
    tags = TextField()
    
class Content(BaseModel):
    id = IntField()
    content = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)
    tags = TextField()  



