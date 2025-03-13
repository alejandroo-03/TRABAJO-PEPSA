from __future__ import print_function
from bd import obtener_conexion
import sys
from funciones_auxiliares import compare_password

def login_usuario(username,password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre, clave FROM usuarios WHERE nombre= %s",(username))
                #cursor.execute("SELECT nombre FROM usuarios WHERE nombre = '" + username +"' and clave= '" + password + "'")
                usuario = cursor.fetchone()
        conexion.close()
        if usuario is None:
            ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
        else:
            passwordIn=usuario[1]
            
            if (compare_password(password.encode("utf-8"),passwordIn.encode("utf-8"))):
                    
                ret = {"status": "OK" }
                #session["usuario"]=username
                #session["nombre"]=usuario[0]
            else:
                ret = {"status":"ERROR"}
        code=200
    except:
          print("Excepcion al validar al usuario")   
          ret={"status":"ERROR"}
          code=500
    return ret,code      
def alta_usuario(username,password,nombre):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
             cursor.execute("SELECT nombre FROM usuarios WHERE nombre = %s and clave= %s",(username,password))
             #cursor.execute("SELECT nombre FROM usuarios WHERE nombre = '" + username +"' and clave= '" + password + "'")
             usuario = cursor.fetchone()
             if usuario is None:
                #print("INSERT INTO usuarios(usuario,clave,nombre) VALUES('"+ username +"','"+  password+"','"+ nombre+"')") 
                cursor.execute("INSERT INTO usuarios(usuario,clave,nombre) VALUES(%s,%s,%s)", (usuario, password, nombre))
                #cursor.execute("INSERT INTO usuarios(usuario,clave,nombre) VALUES('"+ username +"','"+  password+"','"+ nombre+"')")
                if cursor.rowcount == 1:
                    conexion.commit()
                    ret={"status": "OK" }
                    code=200
                else:
                     ret={"status": "ERROR" }
                     code=500
             else:
               ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
               code=200
        conexion.close()
    except:
            print("Excepcion al registrar al usuario")   
            ret={"status":"ERROR"}
            code=500
    return ret,code