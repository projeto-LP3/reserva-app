from conexao_bd import conexao_fechar, conexao_abrir

def salaListar(con):
    cursor = con.cursor()
    sql = "SELECT * FROM sala"
    # Criando o cursor com a opção de retorno como dicionário   
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)

    for (registro) in cursor:
        print(registro['tipo']+ " - "+ registro['capacidade']+ " - "+ registro['descricao']+ " - "+ registro['ativa'])

    cursor.close()

def salaInserir(con, id, tipo, capacidade, descricao, ativa):
     cursor = con.cursor()
     sql = "INSERT INTO sala (id, tipo, capacidade, descricao, ativa) VALUES (%s, %s, %s, %s, %s)"
     cursor.execute(sql, (id, tipo, capacidade, descricao, ativa))
     con.commit() 
     cursor.close()

def salaAtualizar(con, id, tipo=None, capacidade=None, descricao=None, ativa=None):
    cursor = con.cursor()
    sql = "UPDATE sala SET "
    updates = []
    params = []

    if tipo:
        updates.append("tipo = %s")
        params.append(tipo)
    if capacidade:  
        updates.append("capacidade = %s")
        params.append(capacidade)
    if descricao:
        updates.append("descricao = %s")
        params.append(descricao)
    if ativa is not None:
        updates.append("ativa = %s")
        params.append(ativa)

    sql += ", ".join(updates) + " WHERE id = %s"
    params.append(id)

    cursor.execute(sql, params)
    con.commit()
    cursor.close()

def salaDeletar(con, id):
    cursor = con.cursor()
    sql = "DELETE FROM sala WHERE id = %s"
    cursor.execute(sql, (id,))
    con.commit()
    cursor.close()

def usuarioListar(con):
    cursor = con.cursor(dictionary=True)
    sql = "SELECT * FROM usuario"
    cursor.execute(sql)

    for registro in cursor:
        print(f"{registro['id']} - {registro['nome']} - {registro['email']}")

    cursor.close()

def usuarioInserir(con, nome, email, senha):
    cursor = con.cursor()
    sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, email, senha))
    con.commit()
    cursor.close()

def usuarioAtualizar(con, id, nome=None, email=None, senha=None):
    cursor = con.cursor()
    sql = "UPDATE usuario SET "
    updates = []
    params = []

    if nome:
        updates.append("nome = %s")
        params.append(nome)
    if email:
        updates.append("email = %s")
        params.append(email)
    if senha:
        updates.append("senha = %s")
        params.append(senha)

    sql += ", ".join(updates) + " WHERE id = %s"
    params.append(id)

    cursor.execute(sql, params)
    con.commit()
    cursor.close()

def usuarioDeletar(con, id):
    cursor = con.cursor()
    sql = "DELETE FROM usuario WHERE id = %s"
    cursor.execute(sql, (id,))
    con.commit()
    cursor.close()

def main():
    con = conexao_abrir("localhost", "root", "estudante1", "estudante1")
    
    salaInserir(con, "laboratório", 40, "Laboratório de química", True)
    # salaAtualizar(con, 1, tipo="Sala de aula", capacidade=45)
    # salaDeletar(con, 1)
    salaListar(con)

    usuarioInserir(con, "João", "joao@email.com", "abc123")
    # usuarioAtualizar(con, 1, nome="João Guilherme", email="joaogui@example.com")
    # usuarioDeletar(con, 1)
    usuarioListar(con)

    conexao_fechar(con)

if __name__ == "__main__":
    main()



# def obter_salas():
#     with open("cadastro-sala.csv", "r") as file:
#         lista_sala = []
#         for linha in file:
#             id, tipo, descricao, capacidade, ativa = linha.strip().split(",")
#             sala = {
#                 "id": int(id),
#                 "tipo": tipo,
#                 "descricao": descricao,
#                 "capacidade": capacidade,
#                 "ativa": ativa
#             }
#             lista_sala.append(sala)

#         lista_sala.sort(key=lambda x: x['id'])
        
#         return lista_sala
    
# obter_salas()

# def adicionar_sala(s):
#     with open("cadastro-sala.csv", "a") as file:
#         linha = f"{s['id']},{s['tipo']},{s['descricao']},{s['capacidade']},{s['ativa']}\n"
#         file.write(linha)


def busca_binaria_salas(lista, id):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio]['id'] == id:
            return lista[meio]  
        elif lista[meio]['id'] < id:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None

# def obter_usuario():
#     with open("cadastro-usuario.csv", "r") as file:
#         lista_usuario = []
#         for linha in file:
#             nome, email, senha= linha.strip().split(",")
#             usuario = {
#                 "nome": nome,
#                 "email": email,
#                 "senha": senha
#             }
#             lista_usuario.append(usuario)

#         lista_usuario.sort(key=lambda x: x['nome'])
        
#         return lista_usuario

# obter_usuario()

# def adicionar_usuario(u):
#     with open("cadastro-usuario.csv", "a") as file:
#         linha = f"{u['nome']},{u['email']},{u['senha']}\n"
#         file.write(linha)


def busca_binaria_usuarios(lista, nome):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio]['nome'] == nome:
            return lista[meio]
        elif lista[meio]['nome'] < nome:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None

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

obter_reserva()

def adicionar_reserva(u):
    with open("reserva-sala.csv", "a") as file:
        linha = f"{u['sala']},{u['inicio']},{u['fim']}\n"
        file.write(linha)
