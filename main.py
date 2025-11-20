from fastapi import FastAPI
from routes.componentesR import router as componentes
from routes.clientesR import router as clientes
from routes.empleadosR import router as empleados

app = FastAPI()

@app.get("/")
def xd():
    return {"mensaje": "API"}

app.include_router(componentes)
app.include_router(clientes)
app.include_router(empleados)
