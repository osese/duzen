from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime



db = SqliteExtDatabase('example.db')



class BaseModel(Model):
    class Meta:
        database = db 

class Todo(BaseModel):
    id = IntegerField(primary_key=True)
    content = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)
    deadlineDate = DateTimeField(default=datetime.datetime.now)
    is_done = BooleanField(default=False)
    tags = TextField()

    def __repr__(self):
        return str(self.id) +' '+ self.content +' '+ str(self.createdDate) +' '+ str(self.deadlineDate) +' '+ str(self.is_done) +' '+ self.tags
    def __str__(self):
        return str(self.id) +' '+ self.content +' '+ str(self.createdDate) +' '+ str(self.deadlineDate) +' '+ str(self.is_done) +' '+ self.tags
    
class Vocab(BaseModel):
    id = IntegerField(primary_key=True)
    content = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)
    tags = TextField()
    
class Simple(BaseModel):
    id = IntegerField(primary_key=True)
    content = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)
    tags = TextField()  



