from __future__ import print_function
from bd import obtener_conexion
import sys


def convertir_bici_a_json(bici):
    d = {}
    d['id'] = bici[0]
    d['nombre'] = bici[1]
    d['descripcion'] = bici[2]
    d['precio'] = bici[3]
    d['foto'] = bici[4]
    return d

def obtener_bicis():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM bicicletas")
            bicis = cursor.fetchall()
            bicisjson=[]
            if bicis:
                for bici in bicis:
                    bicisjson.append(convertir_bici_a_json(bici))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los bicis", file=sys.stdout)
        bicisjson=[]
        code=500
    return bicisjson,code

def obtener_bici_por_id(id):
    bicijson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM bicicletas WHERE id = %s LIMIT 1", (id,))
            #cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM bicicletas WHERE id =" + id)
            bici = cursor.fetchone()
            if bici is not None:
                bicijson = convertir_bici_a_json(bici)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar una bicicleta", file=sys.stdout)
        code=500
    return bicijson,code

def insertar_bicis(nombre, descripcion, precio,foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO bicicletas(nombre, descripcion, precio,foto) VALUES (%s, %s, %s,%s)",
                       (nombre, descripcion, precio,foto))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar una bicicleta", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def eliminar_bici(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM bicicletas WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar una bicicleta", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_bici(id, nombre, descripcion, precio, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE bicicletas SET nombre = %s, descripcion = %s, precio = %s, foto=%s WHERE id = %s",
                       (nombre, descripcion, precio, foto,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar una bicicleta", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
