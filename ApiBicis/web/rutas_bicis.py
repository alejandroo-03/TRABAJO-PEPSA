import json
from flask import request, session
from __main__ import app
import controlador_bicis as controlador_bicis
from funciones_auxiliares import Encoder, sanitize_input


@app.route("/bicis",methods=["GET"])
def bicis():
    bicis,code= controlador_bicis.obtener_bicis()
    return json.dumps(bicis, cls = Encoder),code

@app.route("/bicis/<id>",methods=["GET"])
def bici_por_id(id):
    id = sanitize_input(id)
    bici,code = controlador_bicis.obtener_bici_por_id(id)
    return json.dumps(bici, cls = Encoder),code

@app.route("/bicis",methods=["POST"])
def guardar_bici():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bici_json = request.json
        nombre = sanitize_input(bici_json["nombre"])
        descripcion = sanitize_input(bici_json["descripcion"])
        precio = sanitize_input(float(bici_json["precio"]))
        foto = sanitize_input(bici_json["foto"])
        
        ret,code=controlador_bicis.insertar_bicis(nombre, descripcion, precio, foto)
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

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
        id = sanitize_input(bici_json["id"])
        nombre = sanitize_input(bici_json["nombre"])
        descripcion = sanitize_input(bici_json["descripcion"])
        precio = sanitize_input(float(bici_json["precio"]))
        foto = sanitize_input(bici_json["foto"])
        ret,code=controlador_bicis.actualizar_bici(id,nombre, descripcion, precio,foto)
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code