from controller import todoW, vocabW, simpleW # import todo, vocab, simple wrapper 
from view import table_view 
from config import VERSION

def main():
    while(1):
        a = input('--> ')    
        a = [x for x in a.split(' ') if(x.strip != '')]

        if(a[0] == 'quit' or a[0] == 'exit'):
            print("Bye bye")
            break 
        if(a[0] == 'version' or a[0] == '-v'):
            print(VERSION)
        elif(len(a) == 1 and a[0] == 'add'):
            b = input('(add) ').strip()
            if(b == 'todo'):
                todoContent = ''
                while(1):
                    a = input('(add)(todo)> ')
                    todoContent += a + '\n'
                    if(a == ''):
                        break
                tags = input('(add)(todo)(tags)> ')

                todoW.add(todoContent, tags)

            elif(b == 'vocab'):
                vocabContent = ''
                while(1):
                    a = input('(add)(vocab)> ')
                    vocabContent += a + '\n'
                    if(a == ''):
                        break
                tags = input('(add)(vocab)(tags)> ')
                if(tags.strip == ''):
                    vocabW.add(vocabContent, '')
                else:
                    vocabW.add(vocabContent, tags) 
                
            elif(b == '' or b == 'simple'):
                simpleContent = ''
                while(1):
                    a = input('(add)(simple)> ')
                    simpleContent += a + '\n'
                    if(a == ''):
                        break
                tags = input('(add)(simple)(tags)> ')
                simpleW.add(simpleContent, tags) 

        elif(len(a) == 1 and a[0] == 'list'):
            b = input('(list) ')
            if(b == 'todo'):
                table_view('todo', todoW.select_all()) # list the all todo content 
        elif(len(a) == 2):
            if(a[0] == 'list' and a[1] == 'todo'):
                table_view('todo', todoW.select_all())
            elif(a[0] == 'list' and a[1] == 'simple'):
                table_view('simple', simpleW.select_all())
            elif(a[0] == 'list' and a[1] == 'vocab'):
                table_view('vocab', vocabW.select_all())
        
        else:
            print('wrong command..')
            continue
        