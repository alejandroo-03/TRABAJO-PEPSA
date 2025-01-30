import os
from flask import Flask
from variables import cargarvariables

app = Flask(__name__)

app.config.from_pyfile('settings.py')
cargarvariables()
  
import rutas_usuarios as rutas_usuarios

import rutas_upload

import rutas_verfichero

import rutas_bicis as rutas_bicis

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)
    
def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:@domain.com" # 