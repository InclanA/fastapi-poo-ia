from fastapi import APIRouter, Depends
from managers.empleadosM import Empleados
from models.models import Empleado
from managers.conexion import getCursor
import psycopg

router = APIRouter(prefix="/empleados", tags=["Empleados"])
manager = Empleados()

@router.get("/")
def obtenerempleados(cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener(cursor)

@router.post("/")
def agregarempleado(empleado: Empleado, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.agregar(empleado, cursor)

@router.put("/{id}")
def actualizarempleado(id: int, datos: Empleado, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.actualizar(id, datos, cursor)

@router.delete("/{id}")
def eliminarempleado(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.eliminar(id, cursor)
