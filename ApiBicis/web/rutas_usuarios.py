from __future__ import print_function
from __main__ import app
from flask import request,session, make_response
from bd import obtener_conexion
import json
import sys
import controlador_usuario
from funciones_auxiliares import *
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
        if "username" in bicicleta_json and "password" in bicicleta_json and "profile" in bicicleta_json and "email" in bicicleta_json:
            username = sanitize_input(bicicleta_json['username'])
            password = sanitize_input(bicicleta_json['password'])
            perfil = sanitize_input(bicicleta_json['profile'])
            email = sanitize_input(bicicleta_json['email'])
            
            if isinstance(username, str) and isinstance(password, str) and isinstance(perfil, str) and len(username) < 50 and len(password) < 50:
                respuesta,code= controlador_usuario.alta_usuario(username,password,perfil,email)
            else:
                respuesta={"status":"Bad parameters"}
                code=403
        else:
            respuesta={"status":"Bad request"}
            code=402
    else:
        respuesta={"status":"Bad format"}
        code=407
    
    return make_response(json.dumps(respuesta, cls=Encoder), code)


@app.route("/logout",methods=['GET'])
def logout():
    try:
        delete_session()
        ret={"status":"OK"}
        code=200
    except:
        ret={"status":"ERROR"}
        code=500
    response=make_response(json.dumps(ret),code)
    return response