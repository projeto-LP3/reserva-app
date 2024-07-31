def obter_salas():
    with open("cadastro-sala.csv", "r") as file:
        lista_sala = []
        for linha in file:
            tipo, descricao, capacidade, ativa = linha.strip().split(",")
            sala = {
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
        linha = f"\n{s['tipo']},{s['descricao']},{s['capacidade']},{s['ativa']}"
        file.write(linha)

s1 = {
    "tipo": "tipo",
    "descricao": "descricao",
    "capacidade": "capacidade",
    "ativa": True   
}

adicionar_sala(s1)
