# 1.- importar fastapi, apirouter y request 
from fastapi import FastAPI, APIRouter, Request, WebSocket, WebSocketDisconnect

# 2.- importar el template del formulario para conectarse al ws
from fastapi.templating import Jinja2Templates

# 3.- indicamos la carpeta donde se creara
templates = Jinja2Templates(directory="templates/")

# comando para arrancar la aplicacion
# ? uvicorn api_multiple:app --reload

# 4.- creamos la app de fastapi y apirouter en su minima expresion
app = FastAPI()
router = APIRouter()

# 5.- Creamos la vista y la app para el formulario
@app.get('/')
def form(request: Request):
    return templates.TemplateResponse(request=request, name='ws/chat.html')

from typing import List

# 6.- definimos el metodo constructor para manejar varias conexiones
class ConnectionManager:
    def __init__(self):
        # lista para almacenar las conexiones activas
        # se inicializa vacias por defecto
        self.active_connections: List[WebSocket] = []

    # 7.- recibimos la conexion del cliente
    async def connect(self, websocket: WebSocket):
        # esperamos que la conexion sea aceptada 
        # tambien podemos manejar eventos y/o validaciones
        await websocket.accept() 
        # agragamos la conexion al array vacio que declaramos mas arriba
        self.active_connections.append(websocket)

    # 8.- desconexion
    def disconnect(self, websocket: WebSocket):
        # remover la conexion de la lista
        self.active_connections.remove(websocket)
    
    # .- enviar mensajes solamente a una persona
    #async def send_personal_message(self, message: str, websocket: WebSocket):
     #   await websocket.send_text(message)
    
    # 9.- iterar el lista de conexiones que tenemos 
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            # enviar mensajes a todos los clientes
            await connection.send_text(message)

manager = ConnectionManager()


# 10.-  creamos una ruta para consumir este websocket
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Cliente #{client_id} dice: {data}")
    
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Cliente #{client_id} se ha desconectado")