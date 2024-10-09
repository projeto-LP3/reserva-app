from conexao_bd import conexao_fechar, conexao_abrir

def clienteListar(con):
    cursor = con.cursor()
    sql = "SELECT * FROM cliente"
    # Criando o cursor com a opção de retorno como dicionário   
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)

    for (registro) in cursor:
        print(registro['cli_nome'] + " - "+ registro['cli_fone'])

    cursor.close()
    #con.commit()    #mesma coisa q editar e não salvar


def clienteInserir(con, codigo, nome, fone, email):
     cursor = con.cursor()
     sql = "INSERT INTO cliente (cli_codigo, cli_nome, cli_fone, cli_email) VALUES (%s, %s, %s, %s)"
     cursor.execute(sql, (codigo, nome, fone, email))
     con.commit() 
     cursor.close()
        

def main():
    con = conexao_abrir("localhost", "root", "", "teste_python")
    
    clienteInserir(con, 10, "evandro", "8876-2222","teste@teste")
    clienteListar(con)

    conexao_fechar(con)


if __name__ == "__main__":
	main()

# -- phpMyAdmin SQL Dump
# -- version 5.2.1
# -- https://www.phpmyadmin.net/
# --
# -- Host: 127.0.0.1
# -- Tempo de geração: 02/10/-- phpMyAdmin SQL Dump
# -- version 5.2.1
# -- https://www.phpmyadmin.net/
# --
# -- Host: 127.0.0.1
# -- Tempo de geração: 02/10/2024 às 16:07
# -- Versão do servidor: 10.4.32-MariaDB
# -- Versão do PHP: 8.2.12

# SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
# START TRANSACTION;
# SET time_zone = "+00:00";


# /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
# /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
# /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
# /*!40101 SET NAMES utf8mb4 */;

# --
# -- Banco de dados: `teste_python`
# --
# CREATE DATABASE IF NOT EXISTS `teste_python` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
# USE `teste_python`;

# -- --------------------------------------------------------

# --
# -- Estrutura para tabela `sala`
# --

# CREATE TABLE `sala` (

#   `id` int(11) NOT NULL,
#   `tipo` varchar(100) NOT NULL,
#   `descricao` varchar(14) NOT NULL,
#   `capacidade` varchar(50) NOT NULL,
# `ativa` varchar(50) NOT NULL,ativa
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;







def obter_salas():
    with open("cadastro-sala.csv", "r") as file:
        lista_sala = []
        for linha in file:
            id, tipo, descricao, capacidade, ativa = linha.strip().split(",")
            sala = {
                "id": int(id),
                "tipo": tipo,
                "descricao": descricao,
                "capacidade": capacidade,
                "ativa": ativa
            }
            lista_sala.append(sala)

        lista_sala.sort(key=lambda x: x['id'])
        
        return lista_sala
    
obter_salas()

def adicionar_sala(s):
    with open("cadastro-sala.csv", "a") as file:
        linha = f"{s['id']},{s['tipo']},{s['descricao']},{s['capacidade']},{s['ativa']}\n"
        file.write(linha)


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

def obter_usuario():
    with open("cadastro-usuario.csv", "r") as file:
        lista_usuario = []
        for linha in file:
            nome, email, senha= linha.strip().split(",")
            usuario = {
                "nome": nome,
                "email": email,
                "senha": senha
            }
            lista_usuario.append(usuario)

        lista_usuario.sort(key=lambda x: x['nome'])
        
        return lista_usuario

obter_usuario()

def adicionar_usuario(u):
    with open("cadastro-usuario.csv", "a") as file:
        linha = f"{u['nome']},{u['email']},{u['senha']}\n"
        file.write(linha)


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
