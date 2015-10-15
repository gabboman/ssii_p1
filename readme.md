Instrucciones:

Testeado en Linux y Windows, no teesteado en OS X

Requisitos: Python3, una cuenta de gmail extra.

Configuración en windows:

1º instalar python 3
2º copiar el archivo integrityChecker.py junto al archivo de configuración settings.json.windows en un directorio seguro y escondido. Por ejemplo C:/Windows/system32/drivers/etc/
3º Editar el archivo settings.json.windows. Dejar first_run a true.
3.1 en digest_path se selecciona la ruta de donde se guardará la lista de hashes de archivo. Se recomienda un lugar dificil de encontrar y que solamente el usuario administrador tenga permiso de escritura
3.2 escribir en to_check la lista de directorios a revisar
3.3 en gmail_user y gmail_passwd se deben colocar un usuario y contraseñas de gmail. Se recomienda una cuenta creada exclusivamente para esta tarea.
3.4 en mail_destination se deberá colocar el correo de destino al cual se enviarán los informes
4º renombrar archivo a settings.json
5º ejecutar integrityChecker.py
6º en el archivo settings, poner first_run a false
7º programar una tarea automatica siguiendo esta guia https://support.microsoft.com/es-es/kb/226795
