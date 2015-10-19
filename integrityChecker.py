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


first_run=settings["first_run"]
dirs2check=settings["direcorios_a_revisar"]
digest_path=settings["digest_path"]
gmail_user=settings["gmail_user"]
gmail_passwd=settings["gmail_passwd"]
destination=settings["destination"]

for d in dirs2check:
    for path, dirs, files in os.walk(d ):
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
        if (not key in second):
            diff[key] = (first[key], KEYNOTFOUND)
        elif (first[key] != second[key]):
            diff[key] = (first[key], second[key])
    # Check all keys in second dict to find missing
    for key in second.keys():
        if (not key in first):
            diff[key] = (KEYNOTFOUND, second[key])
    return diff
diferencia=dict_diff(antiguo,nuevo)

borrados=0
nuevos=0
for a in diferencia:
    if diferencia[a][0]==KEYNOTFOUND:
        nuevos=nuevos+1
    if diferencia[a][1]==KEYNOTFOUND:
        borrados=borrados+1


SUBJECT = 'MAIL_SUBJECT'
TEXT = ''
porcentajeBorrado=borrados*100.0/len(antiguo)
porcentajeModificado=(len(diferencia)-nuevos-borrados*1.0)*100.0/len(antiguo)
if(not len(diferencia) ==0):
    SUBJECT='ERROR: Archivos no integros'
    TEXT= TEXT+"Número de archivos eliminados: "+str(borrados)+'\r\n'
    TEXT= TEXT+"Número de archivos nuevos que no deberían estar: "+str(nuevos)+'\r\n'
    TEXT= TEXT+"Número de archivos modificados: "+str(len(diferencia)-nuevos-borrados)+'\r\n'
else:
    SUBJECT="Archivos integros"
    TEXT='Los archivos continuan integros'

TO = destination


# Gmail Sign In
gmail_sender = gmail_user
gmail_passwd = gmail_passwd

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
