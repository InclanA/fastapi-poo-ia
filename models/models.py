from pydantic import BaseModel

class Componente(BaseModel):
    id: int 
    nombre: str
    marca: str
    modelo: str
    precio: float
    stock: int
    garantia: int 

class Cliente(BaseModel):
    id: int 
    nombre: str
    apellido: str
    email: str
    telefono: str

class Empleado(BaseModel):
    id: int 
    nombre: str
    apellido: str
    legajo: int
    puesto: str
