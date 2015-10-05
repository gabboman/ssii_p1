#/bin/python

#Python 3
#guille es feo
#muy feo
import os
import platform
import hashlib
import codecs
import json
#import configparser, os

#detectar sistema operativo
#print (os.name)
#print (platform.system())
#print ("gabamagar backup. Integrity check system in python. ")
#print(hashlib.sha224(b"texto").hexdigest())

#peleando con abrir archivo y hashearlo
#archivo= open('config.conf')
#print(archivo.read())
#print(hashlib.sha256(archivo.read()).hexdigest())

#peleando con la config
#config = configparser.ConfigParser()
#config.readfp(open('config.conf'))
#config.read(['bitbucket.org', os.path.expanduser('~/.myapp.cfg')])

hashDict= dict()

for path, dirs, files in os.walk('/home/gabriel/ownCloud/workspace'):
    #print (path)
    for f in files:
        archivo= codecs.open(path+'/'+f,'rb')
        hashDict[path+'/'+f]= hashlib.sha256(archivo.read()).hexdigest()
archivo=open('datos.json','w')
json_data = json.dump(hashDict,archivo, sort_keys=True, indent=4)
archivo.close()
