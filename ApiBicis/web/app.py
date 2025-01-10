import os
from flask import Flask
from variables import cargarvariables

app = Flask(__name__)

app.config.from_pyfile('settings.py')
cargarvariables()
  
import web.rutas_usuarios as rutas_usuarios

import rutas_upload

import rutas_verfichero

import web.rutas_bicis as rutas_bicis

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)