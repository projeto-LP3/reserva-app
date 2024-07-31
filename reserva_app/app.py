from flask import Flask, render_template, request, redirect, url_for

from reserva_app.reserva import adicionar_reserva, adicionar_sala, adicionar_usuario, obter_salas
    
# lista_sala = [ 
#     {"id": "1", "tipo": "Sala de aula", "descricao": "PCs com intel i5, 8GB de RAM", "capacidade": "20", "ativa": True}
# ]

# lista_usuario = [ 
#     {"nome": "ana", "email": "maya@email.com", "senha": "sbhsgksg"}
# ]

# lista_reseva = [ 
#     {"sala": "1", "inicio": "Sala de aula", "d": "PCs com intel i5, 8GB de RAM", "capacidade": "20", "ativa": True}
# ]

app = Flask("minha app")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/templates/login")
def loginCadastro():
    return render_template("login.html")

@app.route("/templates/cadastrar-sala")
def cadastrarsala():
    return render_template("cadastrar-sala.html")

@app.route("/templates/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/templates/cadastro", methods=["POST"])
def cadastro_us():
    nome=request.form['nome']
    email=request.form['email']
    senha=request.form['senha']
    usuario= {"nome": nome,"email": email, "senha": senha}

    adicionar_usuario(usuario)

    return redirect(url_for("login"))

@app.route("/templates/listar-salas")
def listar_salas():
    return render_template("listar-salas.html", salas=obter_salas())

@app.route("/templates/cadastrar-sala", methods=["POST"])
def adicionar_salaus():
    id=1
    tipo=request.form['tipo']
    descricao=request.form['descricao']
    capacidade=request.form['capacidade']
    ativa=True
    sala= {"id": id,"tipo": tipo, "descricao": descricao, "capacidade": capacidade, "ativa": ativa}

    adicionar_sala(sala)


    return redirect(url_for("listar_salas"))

@app.route("/templates/reservar-sala")
def reservarsala():
    return render_template("reservar-sala.html", salas=obter_salas())



@app.route("/templates/reservas")
def reservas():
    return render_template("reservas.html")

@app.route("/templates/reservar-sala", methods=["POST"])
def adicionar_reservaus():
    sala=request.form['sala']
    inicio=request.form['inicio']
    fim=request.form['fim']
    reserva= {"sala": sala,"inicio": inicio, "fim": fim}

    adicionar_reserva(reserva)

    
    return redirect(url_for("adicionar_reservaus"))


@app.route("/templates/reserva/detalhe-reserva")
def detalhe_reserva():
    return render_template("detalhe-reserva.html")


app.run(port=5001)