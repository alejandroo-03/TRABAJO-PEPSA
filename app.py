import os
from dotenv import load_dotenv
from flask import Flask, render_template
#from variables import cargarVariables

app = Flask(__name__)

app.config.from_pyfile('settings.py')
#cargarVariables()

@app.route("/")
def inicio():
    return render_template("index.html")
    
#import rutas_inicio

#import rutas_juegos

if __name__ == '__main__':
    port = 8080 #int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)