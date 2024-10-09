from flask import Flask, render_template, request, redirect, url_for
import random
import psycopg2
from juego import juego_bp

app = Flask(__name__)

# Configuración de PostgreSQL (ajusta a tu configuración)
# conn = psycopg2.connect("dbname=tu_db user=tu_usuario password=tu_password host=localhost")

@app.route('/registro', methods = ['GET', 'POST'])
def registro():
    return render_template('registro.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(juego_bp, url_prefix='/juego')

if __name__ == '__main__':
    app.run(debug=True)

