import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask import redirect, url_for, render_template, request
#from variables import cargarVariables

app = Flask(__name__)

app.config.from_pyfile('settings.py')
#cargarVariables()



@app.route("/")
def inicio():
    return render_template("index.html")
    

@app.route("/login", methods = ["POST"])
def login():
    
    usuario = request.form.get("username")
    
    passwd = request.form.get("password")
    
    if usuario == passwd:
        error = "Correcto"
    else:
        error = "ERROR"
    
    return render_template("index.html", error=error)





    
#import rutas_inicio

#import rutas_juegos


# esto es para lanzar la aplicacion
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
if __name__ == '__main__':
    port = 8080 #int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)