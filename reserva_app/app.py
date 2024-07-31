from flask import Flask, render_template, request, redirect, url_for
    
lista_sala = [ 
    {"tipo": "Sala de aula", "descricao": "PCs com intel i5, 8GB de RAM", "capacidade": "20", "ativa": True}
]

app = Flask("minha app")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/templates/cadastrar-sala")
def cadastrarsala():
    return render_template("cadastrar-sala.html")

@app.route("/templates/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/templates/listar-salas")
def listarsalas():
    return render_template("listar-salas.html", salas=lista_sala)

@app.route("/listar-salas", methods=["POST"])
def adicionar_sala():
    tipo=request.form['tipo']
    descricao=request.form['descricao']
    capacidade=request.form['capacidade']
    ativa=request.form['ativa']
    sala= {"tipo": tipo, "descricao": descricao, "capacidade": capacidade, "ativa": ativa}
    lista_sala.append(sala)

    return redirect(url_for("listar-salas"))

@app.route("/templates/reservar-sala")
def reservarsala():
    return render_template("reservar-sala.html")

@app.route("/templates/reservas")
def reservas():
    return render_template("reservas.html")


app.run(port=5001)