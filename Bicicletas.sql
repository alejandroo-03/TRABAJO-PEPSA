CREATE DATABASE IF NOT EXISTS DEATHBIKES;
USE DEATHBIKES;
CREATE TABLE IF NOT EXISTS bicicletas{
    id int auto_increment unsigned not null primary key,
    precio decimal (8,2) not null,
    color varchar (255) not null,
    modelo varchar (255) not null, 
    tipo varchar (255) not null, 
};