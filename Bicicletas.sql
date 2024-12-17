CREATE DATABASE IF NOT EXISTS DEATHBIKES;
USE DEATHBIKES;
CREATE TABLE IF NOT EXISTS bicicletas{
    id int auto_increment unsigned not null primary key,
    precio decimal (8,2) not null,
    color varchar (255) not null,
    modelo varchar (255) not null, 
    tipo varchar (255) not null, 
};

CREATE TABLE color (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    cod_hexa VARCHAR (50),
);

-- Puedes agregar datos iniciales si lo necesitas
INSERT INTO bicicletas (id, precio, color, modelo, tipo) VALUES ('1', '6500', 'Satin Cooper/Smoke', 'Roubaix SL8 Expert', 'Carretera');
INSERT INTO color (id, nombre, cod_hexa) VALUES ('1', 'Satin Cooper/Smoke', '#73372d')