1.- lo primero es activar el entorno virtual:
ctrl + shift + p = pyhton envirorment -> .venv -> seleccionar la
opcion que haya en la maquina y esperar a que se active el entorno

2.- instalar fastapi: 
pip install fastapi

3.- instalar uvicorn:
pip install uvicorn

4.- instalar web sockets:
pip install websockets

* (se debera invocar cada vez que se instale una dependencia con pip)5.- invocar el archivo requirements.txt que contendra
las dependencias necesarias para que funcione la app
pip freeze > requirements.txt

6.- creamos el archivo .gitignore para proyecto fastapi (chat ia vscode)

7.- instalar template para consumir el websocket
pip install jinja2 -> paso 5
