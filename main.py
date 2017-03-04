import prompt 
from model import db
from datetime import datetime
import shutil 


#db.connect()    


prompt.main()


db.close()

a = datetime.now()
file_name = str(a.day) +'-'+ str(a.hour)+'-'+ str(a.minute) +'-'+ str(a.second)+'.db'
shutil.copy('./example.db', './backup/'+ file_name)

