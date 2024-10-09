from flask import Blueprint, render_template, request
from dados import Dados

# Crear el Blueprint para las rutas del juego
juego_bp = Blueprint('juego', __name__, template_folder='templates/juego')

@juego_bp.route('/nivel')
def nivel():
    return render_template('nivel.html')

@juego_bp.route('/juego1')
def juego1():
    # Nivel fácil: Tira 1 dado
    dados = Dados(cantidad=1)
    resultado = dados.tirar()
    return render_template('juego1.html', resultado=resultado)

@juego_bp.route('/juego2')
def juego2():
    # Nivel normal: Tira 2 dados
    dados = Dados(cantidad=2)
    resultado = dados.tirar()
    return render_template('juego2.html', resultado=resultado)

@juego_bp.route('/juego3')
def juego3():
    # Nivel experto: Tira 3 dados
    dados = Dados(cantidad=3)
    resultado = dados.tirar()
    return render_template('juego3.html', resultado=resultado)
