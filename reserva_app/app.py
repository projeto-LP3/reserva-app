    # Iniciar o projeto usando o código https://github.com/domingoslatorre/reserva-app
    # Implementar os seguintes requisitos para todas as páginas:
    # Rotas para todas as páginas
    # Uso de templates e layouts
    # Cadastrar sala e listar sala - arquivo csv
    # Reservar sala - arquivo csv
    # Cadastro usuário - arquivo csv
from flask import Flask, render_template

app = Flask("Meu app")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/cadastrar-sala")
def cadastrarsala():
    return render_template("cadastrar-sala.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/listar-salas")
def listarsalas():
    return render_template("listar-salas.html")

@app.route("/reservar-sala")
def reservarsala():
    return render_template("reservar-sala.html")

@app.route("/reservas")
def reservas():
    return render_template("reservas.html")