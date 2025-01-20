from __future__ import print_function
from __main__ import app
from flask import request,session
from bd import obtener_conexion
import json
import sys
import controlador_usuario
from funciones_auxiliares import Encoder

@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bicicleta_json = request.json
        username = bicicleta_json['username']
        password = bicicleta_json['password']
        respuesta,code = controlador_usuario.login_usuario(username,password)
        return json.dumps(respuesta, cls = Encoder),code
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/registro",methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bicicleta_json = request.json
        username = bicicleta_json['username']
        password = bicicleta_json['password']
        perfil = bicicleta_json['profile']
        respuesta,code=controlador_usuario.alta_usuario(username,password,perfil)
        return json.dumps(respuesta, cls = Encoder), code
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code


@app.route("/logout", methods=['GET'])
def logout():
    
    response = json.dumps({"status": "OK"})
    return response, 200, {'Content-Type': 'application/json'}
