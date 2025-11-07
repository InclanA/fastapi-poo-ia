from fastapi import APIRouter, Depends
from managers.clienteM import Clienter
from models.models import Cliente
from managers.conexion import getCursor
import psycopg

router = APIRouter(prefix="/clientes", tags=["Clientes"])
manager = Clienter()

@router.get("/")
def obtenerclientes(cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener(cursor)

@router.post("/")
def agregarcliente(cliente: Cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.agregar(cliente, cursor)

@router.put("/{id}")
def actualizarcliente(id: int, datos: Cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.actualizar(id, datos, cursor)

@router.delete("/{id}")
def eliminarcliente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.eliminar(id, cursor)
