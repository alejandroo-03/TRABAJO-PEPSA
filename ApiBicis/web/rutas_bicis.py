import json
from flask import request, session, make_response
from __main__ import app
import controlador_bicis #as controlador_bicis
from funciones_auxiliares import Encoder, sanitize_input, prepare_response_extra_headers,validar_session_admin,validar_session_normal


@app.route("/bicis",methods=["GET"])
def bicis():
    if (validar_session_normal()):
        respuesta,code= controlador_bicis.obtener_bicis()
    else:
        respuesta={"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

    #bicis,code= controlador_bicis.obtener_bicis()
    #return json.dumps(bicis, cls = Encoder),code

@app.route("/bicis/<id>",methods=["GET"])
def bici_por_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id)<64:
        if (validar_session_normal()):
            respuesta,code = controlador_bicis.obtener_bici_por_id(id)
        else:
            respuesta={"status":"Forbidden"}
            code=403
    else:
        respuesta={"status":"Bad parameters"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response
    #id = sanitize_input(id)
    #bici,code = controlador_bicis.obtener_bici_por_id(id)
    #return json.dumps(bici, cls = Encoder),code

@app.route("/bicis",methods=["POST"])
def guardar_bici():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bici_json = request.json
        if "nombre" in bici_json and "descripcion" in bici_json and "foto" in bici_json:
            nombre = sanitize_input(bici_json["nombre"])
            descripcion = sanitize_input(bici_json["descripcion"])
            precio = bici_json["precio"]
            foto = sanitize_input(bici_json["foto"])
            
            if isinstance(nombre, str) and isinstance(descripcion, str) and isinstance(foto, str) and len(nombre)<128 and len(descripcion)<512 and len(foto)<128:
                if (validar_session_admin()):
                    precio = float(precio)
                    respuesta,code=controlador_bicis.insertar_bicis(nombre,descripcion,precio,foto)
                else: 
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder))  
    return response

        #bici_json = request.json
        #nombre = sanitize_input(bici_json["nombre"])
        #descripcion = sanitize_input(bici_json["descripcion"])
        #precio = sanitize_input(float(bici_json["precio"]))
        #foto = sanitize_input(bici_json["foto"])
        
        #ret,code=controlador_bicis.insertar_bicis(nombre, descripcion, precio, foto)
    #else:
        #ret={"status":"Bad request"}
        #code=401
    #return json.dumps(ret), code

@app.route("/bicis/<id>", methods=["DELETE"])
def eliminar_bici(id):
    id = sanitize_input(id)
    ret,code=controlador_bicis.eliminar_bici(id)
    return json.dumps(ret), code

@app.route("/bicis", methods=["PUT"])
def actualizar_bici():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bici_json = request.json
        if "id" in bici_json and "nombre" in bici_json and "descripcion" in bici_json and "foto" in bici_json:
            id = request.json["id"]
            nombre = sanitize_input(bici_json["nombre"])
            descripcion = sanitize_input(bici_json["descripcion"])
            precio = bici_json["precio"]
            foto = sanitize_input(bici_json["foto"])
            
            if id.isnumeric() and isinstance(nombre, str) and isinstance(descripcion, str) and precio.isnumeric() and isinstance(foto, str) and len(id)<8 and len(nombre)<128 and len(descripcion)<512 and len(foto)<128:
                id=int(id)
                precio=float(precio)
                if (validar_session_normal()):
                    respuesta,code=controlador_bicis.actualizar_bici(id,nombre,descripcion,precio,foto,)
                else: 
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response
    #if (content_type == 'application/json'):
#        bici_json = request.json
#        id = sanitize_input(bici_json["id"])
#        nombre = sanitize_input(bici_json["nombre"])
#        descripcion = sanitize_input(bici_json["descripcion"])
#        precio = sanitize_input(float(bici_json["precio"]))
#        foto = sanitize_input(bici_json["foto"])
#        ret,code=controlador_bicis.actualizar_bici(id,nombre, descripcion, precio,foto)
#    else:
#        ret={"status":"Bad request"}
#        code=401
#    return json.dumps(ret), code