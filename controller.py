from model import db, Todo,Vocab,Simple
import config


# db.connect()

if(not db.get_tables()):
    db.create_tables([Todo, Vocab, Simple])

# new = Todo.create(id=2,content="selam naber",tags="Useless,")
# newV = Vocab.create(id=1,content="selam: naber", tags="Useless,")
# newC = Content.create(id=1,content="Selam naber.", tags="Useless,")

# todo Wrapper class      
class todoW:
    def select_all(): # todo select all
        # return [x for x in Todo.select()]
        return Todo.select()

    def add(content, tags):
        a = Todo.create(content=content, tags = tags) # this is an insert query 

    def update_is_done(id):
        a = Todo.update(is_done=True).where(Todo.id == id)   
        return a.execute()

    def delete_by_id(id):
        a = Todo.select().where(Todo.id==id)
        a.delete_instance()
        
    def add_tag_by_id(id, _tags):
        a = Todo.update(tags=_tags).where(Todo.id==id)
        return a.execute()

class simpleW:
    def select_all(): # todo select all
        # return [x for x in Todo.select()]
        return Simple.select()

    def add(content, tags):
        a = Simple.create(content=content, tags = tags) # this is an insert query 

class vocabW:
    def select_all(): # todo select all
        # return [x for x in Todo.select()]
        return Vocab.select()

    def add(content, tags):
        a = Vocab.create(content=content, tags = tags) # this is an insert query 

