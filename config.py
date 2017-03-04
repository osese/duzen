import json
NAME = ''
VERSION = ''
DEBUG = '1'
OPENED = '0'



with open('config.json') as f:
    data = json.load(f)

NAME = data['name']
VERSION = data['version']
OPENED = data['opened']
DEBUG = data['debug']
DESCRIPTION  = data['description']

if(data['opened'] == '0'):
    data['opened'] = '1'
    OPENED = '1'
    with open('config.json','w') as f:
        json.dump(data, f)

