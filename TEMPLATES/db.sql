drop database  administrador_db;
create database administrador_db;
use administrador_db;
create table usuarios(
    id int primary key auto_increment,
    codigo varchar(40),
    nombre varchar(40),
    correo varchar(40),
    perfil varchar(40)
);

Insert into usuarios(codigo, nombre, correo, perfil) values ('20201313','Tomas','tomas1@abc.com', 'Usuario');

create table eventos(
    id int primary key auto_increment,
    titulo varchar(40),
    fecha date,
    espacios varchar(40),
    descripcion varchar(40)
);

Insert into eventos(titulo, fecha, espacios, descripcion) values ('Evento A','2023-10-15', '15', 'Evento de 5 horas.');
