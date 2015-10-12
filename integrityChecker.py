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

nuevo= dict()

for path, dirs, files in os.walk('/home/gabriel/ownCloud/workspace'):
    #print (path)
    for f in files:
        archivo= codecs.open(path+'/'+f,'rb')
        nuevo[path+'/'+f]= hashlib.sha256(archivo.read()).hexdigest()
#archivo=open('datos.json','w')
#json_data = json.dump(nuevo,archivo, sort_keys=True, indent=4)
#archivo.close()

archivo=open('datos.json','r')
#contenido=archivo.read()
antiguo=json.load(archivo)
#print(yeison["/home/gabriel/ownCloud/workspace/HighfredoBot/.git/COMMIT_EDITMSG"])

#print(antiguo==nuevo)


KEYNOTFOUND = 'NO_FILE'       # KeyNotFound for dictDiff

def dict_diff(first, second):#Metodo encontrado en internet

    """ Return a dict of keys that differ with another config object.  If a value is
        not found in one fo the configs, it will be represented by KEYNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dicationary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    diff = {}
    # Check all keys in first dict
    for key in first.keys():
        if (not second.has_key(key)):
            diff[key] = (first[key], KEYNOTFOUND)
        elif (first[key] != second[key]):
            diff[key] = (first[key], second[key])
    # Check all keys in second dict to find missing
    for key in second.keys():
        if (not first.has_key(key)):
            diff[key] = (KEYNOTFOUND, second[key])
    return diff
diferencia=dict_diff(antiguo,nuevo)
