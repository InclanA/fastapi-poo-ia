import psycopg
from models.models import Cliente, Empleado

class Clienter:
    def agregar(self, cliente: Cliente, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s)",
            (cliente.nombre, cliente.apellido, cliente.email, cliente.telefono),
        )
        return "Cliente creado"

    def clientes(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT id, nombre, apellido, email, telefono FROM cliente").fetchall()
        return [{"id": row[0], "nombre": row[1], "apellido": row[2], "email": row[3], "telefono": row[4]} for row in res]

    def clienteporId(self, id: int, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT id, nombre, apellido, email, telefono FROM cliente WHERE id = %s", (id,)
        ).fetchall()
        return [{"id": row[0], "nombre": row[1], "apellido": row[2], "email": row[3], "telefono": row[4]} for row in res]

    def Editar(self, id: int, updatedCliente: Cliente, cursor: psycopg.Cursor) -> str:
        cursor.execute(
            "UPDATE cliente SET nombre = %s, apellido = %s, email = %s, telefono = %s WHERE id = %s",
            (updatedCliente.nombre, updatedCliente.apellido, updatedCliente.email, updatedCliente.telefono, id),
        )
        return "Cliente modificado"

    def eliminar(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))
        return "Cliente eliminado"

