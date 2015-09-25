#Python 3
#guille es feo
#muy feo
import os
import platform
import hashlib
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

for path, dirs, files in os.walk('/home/practica/gabamagar'):
  print (path)
  for f in files:
  	archivo= open(path+'/'+f)
  	print (path+'/'+f+' sha256: ' + hashlib.sha256(archivo.read()).hexdigest() )