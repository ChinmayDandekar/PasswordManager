from test import decryptit

class pas():
    name:str
    password:str


obj1 = pas()
obj1.name = 'a'
obj1.password = '4eKrRihQYsPWZuq4ydl5qTAxPcYMX9TWY6fnWDYaF+s='

obj2 = pas()
obj2.name = 'a'
obj2.password = '4eKrRihQYsPWZuq4ydl5qTAxPcYMX9TWY6fnWDYaF+s='

obj3 = pas()
obj3.name = 'a'
obj3.password = '4eKrRihQYsPWZuq4ydl5qTAxPcYMX9TWY6fnWDYaF+s='

obj4 = pas()
obj4.name = 'a'
obj4.password = '4eKrRihQYsPWZuq4ydl5qTAxPcYMX9TWY6fnWDYaF+s='



passs = [obj1,obj2,obj3,obj4]
for i in passs:
    i.password = 'a'
    print (i.password)