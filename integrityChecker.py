#/bin/python

#Python 3
#
import os
import hashlib
import codecs
import json

archivo=open('settings.json','r')
settings=json.load(archivo)

first_run=settings["first_run"]
digest_path=settings["digest_path"]
gmail_user=settings["gmail_user"]
gmail_passwd=settings["gmail_passwd"]
to_check=settings["to_check"]
exclude=settings["exclude"]

nuevo= dict()
for location in to_check:
    for path, dirs, files in os.walk(location):
        if path not in exclude:
            for f in files:
                archivo= codecs.open(path+'/'+f,'rb')
                nuevo[path+'/'+f]= hashlib.sha256(archivo.read()).hexdigest()
if(first_run):
    archivo=open(digest_path,'w')
    json_data = json.dump(nuevo,archivo, sort_keys=True, indent=4)
    archivo.close()

archivo=open(digest_path,'r')
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

print (diferencia)
