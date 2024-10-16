CREATE DATABASE estudante1;

USE estudante1;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    senha VARCHAR(255)
);

CREATE TABLE sala (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    capacidade INT NOT NULL,
    descricao TEXT,
    ativa BOOLEAN NOT NULL
);

SELECT * 
FROM usuario;

SELECT * 
FROM sala;
