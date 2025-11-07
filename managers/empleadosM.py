
import psycopg
from models.models import  Empleado , Cliente

class Empleados:
    def agregar(self, empleado: Empleado, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO empleado (nombre, apellido, legajo, puesto) VALUES (%s, %s, %s, %s)",
            (empleado.nombre, empleado.apellido, empleado.legajo, empleado.puesto),
        )
        return "Empleado creado"

    def empleados(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT id, nombre, apellido, legajo, puesto FROM empleado").fetchall()
        return [{"id": row[0], "nombre": row[1], "apellido": row[2], "legajo": row[3], "puesto": row[4]} for row in res]

    def empleadoForId(self, id: int, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT id, nombre, apellido, legajo, puesto FROM empleado WHERE id = %s", (id,)
        ).fetchall()
        return [{"id": row[0], "nombre": row[1], "apellido": row[2], "legajo": row[3], "puesto": row[4]} for row in res]

    def editar(self, id: int, updatedEmpleado: Empleado, cursor: psycopg.Cursor) -> str:
        cursor.execute(
            "UPDATE empleado SET nombre = %s, apellido = %s, legajo = %s, puesto = %s WHERE id = %s",
            (updatedEmpleado.nombre, updatedEmpleado.apellido, updatedEmpleado.legajo, updatedEmpleado.puesto, id),
        )
        return "Empleado modificado"

    def eliminar(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM empleado WHERE id = %s", (id,))
        return "Empleado eliminado"
