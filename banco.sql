

USE cadastro;
SELECT * FROM pessoas;

create table pessoas (
nome varchar(30),
idade tinyint,
sexo char(1),
peso float,
altura float,
nacionalidade varchar(20)
);

create table salario (
id int auto_increment primary key,
valor decimal(10,2),
cargo varchar(30),
data_pagamento date,
setor varchar(30)
);

INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade)
VALUES ('Israel de Albuquerque', 20, 'M', 80.0, 1.75, 'Brasil');
