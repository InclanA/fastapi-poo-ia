import psycopg
from models.models import Componente, Cliente, Empleado


class Componentes:
    def agregar(self, componente: Componente, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO componente (nombre, marca, modelo, precio, stock, garantia) VALUES (%s,%s,%s,%s,%s,%s)",
            (componente.nombre, componente.marca, componente.modelo, componente.precio, componente.stock, componente.garantia),
        )
        return "Componente agregado"

    def componentes (self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT id, nombre, marca, modelo, precio, stock, garantia FROM componente").fetchall()
        return [
            {"id": row[0], "nombre": row[1], "marca": row[2], "modelo": row[3], "precio": row[4], "stock": row[5], "garantia": row[6]}
            for row in res
        ]

    def Componenteporid(self, id: int, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT id, nombre, marca, modelo, precio, stock, garantia FROM componente WHERE id = %s", (id,)
        ).fetchall()
        return [
            {"id": row[0], "nombre": row[1], "marca": row[2], "modelo": row[3], "precio": row[4], "stock": row[5], "garantia": row[6]}
            for row in res
        ]

    def modificar(self, id: int, updated: Componente, cursor: psycopg.Cursor) -> str:
        cursor.execute(
            "UPDATE componente SET nombre = %s, marca = %s, modelo = %s, precio = %s, stock = %s, garantia = %s WHERE id = %s",
            (updated.nombre, updated.marca, updated.modelo, updated.precio, updated.stock, updated.garantia, id),
        )
        return "Componente modificado"

    def eliminar(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM componente WHERE id = %s", (id,))
        return "Componente eliminado"
