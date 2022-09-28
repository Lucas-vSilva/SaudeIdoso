create database saudeidoso;
use saudeidoso;

create table cuidador(
cod int not null auto_increment primary key,
email varchar(150) not null,
telefone bigint(11) not null, 
cpf bigint(11) not null, 
sexo varchar(10) not null,
rg bigint(9) not null,
user varchar(20) not null,
pswd varchar(40) not null
) Engine = InnoDB;

create table cliente(
cod int not null auto_increment primary key,
nome varchar(150) not null,
apelido varchar (50) not null,
sus bigint(15) not null,
rg bigint(9) not null,
cpf bigint(11) not null,
dataNascimento date not null,
sexo varchar(10) not null,
uf varchar(150) not null,
nacionalidade varchar(150) not null,
paisNascimento varchar(150) not null, 
alfabetizado varchar(3) not null,
escolaridade varchar(50) not null,
etnia varchar(50) not null,
religião varchar(50) not null,
email varchar(150) not null,
user varchar(20) not null,
pswd varchar(40) not null
) Engine = InnoDB;

create table abaMonitoramento(
cod int not null auto_increment primary key,
pressão varchar(150) not null,
diabete float not null,
dieta varchar(150) not null,
kilo float not null,
altura decimal(10,2)
) Engine = InnoDB;

create table abaAgenda(
cod int not null auto_increment primary key,
exame date not null, 
consulta date not null
)Engine = InnoDB;

