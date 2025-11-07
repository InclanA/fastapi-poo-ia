from fastapi import APIRouter, Depends
from managers.componentesM import Componentes
from models.models import Componente
from managers.conexion import getCursor
import psycopg

router = APIRouter(prefix="/componentes", tags=["Componentes"])
manager = Componentes()

@router.get("/")
def obtenercomponentes(cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.componentes(cursor)

@router.post("/")
def agregarcomponente(componente: Componente, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.agregar(componente, cursor)

@router.put("/{id}")
def actualizarcomponente(id: int, datos: Componente, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.modificar(id, datos, cursor)

@router.delete("/{id}")
def eliminarcomponente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.eliminar(id, cursor)
