import json
from flask import request, session
from __main__ import app
import controlador_bicis as controlador_bicis
from funciones_auxiliares import Encoder


@app.route("/bicis",methods=["GET"])
def bicis():
    bicis,code= controlador_bicis.obtener_bicis()
    return json.dumps(bicis, cls = Encoder),code

@app.route("/bicis/<id>",methods=["GET"])
def bici_por_id(id):
    bici,code = controlador_bicis.obtener_bici_por_id(id)
    return json.dumps(bici, cls = Encoder),code

@app.route("/bicis",methods=["POST"])
def guardar_bici():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bici_json = request.json
        ret,code=controlador_bicis.insertar_bicis(bici_json["nombre"], bici_json["descripcion"], float(bici_json["precio"]), bici_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/bicis/<id>", methods=["DELETE"])
def eliminar_bici(id):
    ret,code=controlador_bicis.eliminar_bici(id)
    return json.dumps(ret), code

@app.route("/bicis", methods=["PUT"])
def actualizar_bici():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bici_json = request.json
        ret,code=controlador_bicis.actualizar_bici(bici_json["id"],bici_json["nombre"], bici_json["descripcion"], float(bici_json["precio"]),bici_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code