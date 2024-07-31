def obter_salas():
    with open("cadastro-sala.csv", "r") as file:
        lista_sala = []
        for linha in file:
            id, tipo, descricao, capacidade, ativa = linha.strip().split(",")
            sala = {
                "id": id,
                "tipo": tipo,
                "descricao": descricao,
                "capacidade": capacidade,
                "ativa": ativa
            }
            lista_sala.append(sala)
        
        return lista_sala
    
obter_salas()

def adicionar_sala(s):
    with open("cadastro-sala.csv", "a") as file:
        linha = f"{s['id']},{s['tipo']},{s['descricao']},{s['capacidade']},{s['ativa']}\n"
        file.write(linha)



# adicionar_sala(s1)

def obter_usuario():
    with open("cadastro-usuario.csv", "r") as file:
        lista_sala = []
        for linha in file:
            nome, email, senha= linha.strip().split(",")
            usuario = {
                "nome": nome,
                "email": email,
                "senha": senha
            }
            lista_sala.append(usuario)
        
        return lista_sala

obter_usuario()

def adicionar_usuario(u):
    with open("cadastro-usuario.csv", "a") as file:
        linha = f"{u['nome']},{u['email']},{u['senha']}\n"
        file.write(linha)

def obter_reserva():
    with open("reserva-sala.csv", "r") as file:
        lista_reserva = []
        for linha in file:
            sala, inicio, fim= linha.strip().split(",")
            reserva = {
                "sala": sala,
                "inicio": inicio,
                "fim": fim
            }
            lista_reserva.append(reserva)
        
        return lista_reserva

obter_usuario()

def adicionar_reserva(u):
    with open("reserva-sala.csv", "a") as file:
        linha = f"{u['sala']},{u['inicio']},{u['fim']}\n"
        file.write(linha)