from __future__ import print_function
from __main__ import app
from flask import request,session
from bd import obtener_conexion
import json
import sys
import controlador_usuario
from funciones_auxiliares import Encoder, sanitize_input
import bleach

@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bicicleta_json = request.json
        
        if "username" in bicicleta_json and "password" in bicicleta_json: 
            username = sanitize_input(bicicleta_json['username'])
            password = sanitize_input(bicicleta_json['password'])
            
            if isinstance(username,str) and isinstance(password,str) and len(username) < 50 and len(password) < 50:
                ret,code = controlador_usuario.login_usuario(username,password)
            else:
                ret={"status":"Bad request"}
                code=401 

        else:
            ret={"status":"Missing parameters"}
            code=401     
            
    else:
        ret={"status":"Bad request"}
        code=401
        
    return json.dumps(ret), code

@app.route("/registro",methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        bicicleta_json = request.json
        username = sanitize_input(bicicleta_json['username'])
        password = sanitize_input(bicicleta_json['password'])
        perfil = sanitize_input(bicicleta_json['profile'])
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
