# 1.- importar fastapi, apirouter y request 
from fastapi import FastAPI, APIRouter, Request, WebSocket

# 2.- importar el template del formulario para conectarse al ws
from fastapi.templating import Jinja2Templates

# 3.- indicamos la carpeta donde se creara
templates = Jinja2Templates(directory="templates/")

# comando para arrancar la aplicacion
# ? uvicorn api:app --reload

# 4.- creamos la app de fastapi y apirouter en su minima expresion
app = FastAPI()
router = APIRouter()

# 5.- Creamos la vista y la app para el formulario
@app.get('/')
def form(request: Request):
    return templates.TemplateResponse(request=request, name='ws/chat.html')

# 7.- creamos el websocket (sin http: no get, post, put, patch, delete)
@app.websocket("/ws")
# * esperamos la conexion al wss
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept() # ! aceptamos la conexion
    while True: 
# * esto se ejectura en bucle hasta que se reciba una respuesta del usuario
        data = await websocket.receive_text()
        # * enviamos la data de vuelta
        await websocket.send_text(f"Message text was: {data}")
