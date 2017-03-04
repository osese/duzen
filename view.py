def table_view(ty, li):
    if(ty == 'todo'):
        for i in li: 
            print(' | ', i.id, end='')
            print(' | ', i.content[0:10],'....', end='')
            print(' | ', i.createdDate, end='')
            print(' | ', i.deadlineDate, end='')
            print(' | ', i.is_done, end='')
            print(' | ', i.tags, end='')
            print()
            
    elif(ty == 'simple'):
        for i in li: 
            print(' | ', i.id, end='')
            print(' | ', i.content[0:10],'....', end='')
            print(' | ', i.createdDate, end='')
            print(' | ', i.tags, end='')
            print()
    elif(ty == 'vocab'):
        for i in li: 
            print(' | ', i.id, end='')
            print(' | ', i.content[0:10],'....', end='')
            print(' | ', i.createdDate, end='')
            print(' | ', i.tags, end='')
            print()