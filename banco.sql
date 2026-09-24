

USE cadastro;
SELECT * FROM usuario;

create table usuario (
nome varchar(30),
idade tinyint,
sexo char(1),
peso float,
altura float,
cpf varchar(11)
);

create table salario (
id int auto_increment primary key,
valor decimal(10,2),
cargo varchar(30),
data_pagamento date,
setor varchar(30)
);

INSERT INTO usuario (nome, idade, sexo, peso, altura, cpf)
VALUES ('Israel de Albuquerque', 20, 'M', 80.0, 1.75, '12345678901');
