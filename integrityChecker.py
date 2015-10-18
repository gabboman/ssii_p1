#/bin/python3

import os
import platform
import hashlib
import codecs
import json
#import configparser, os


nuevo= dict()
settingsf=open("settings.json")
settings=json.load(settingsf)
dirs2check=settings["direcorios_a_revisar"]
print (dirs2check)
for d in dirs2check:
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
print diferencia
