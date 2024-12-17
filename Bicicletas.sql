CREATE DATABASE IF NOT EXISTS DEATHBIKES;
USE DEATHBIKES;
CREATE TABLE IF NOT EXISTS bicicletas{
    id int auto_increment unsigned not null primary key,
    precio decimal (8,2) not null,
    color varchar (255) not null,
    modelo varchar (255) not null, 
    tipo varchar (255) not null, 
};

-- Agregamos inserts
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('6500', 'Satin Cooper/Smoke', 'Roubaix SL8 Expert', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('7500', 'Blanco Mate', 'Venge Pro', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('8200', 'Rojo Brillante', 'Tarmac SL7', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('9200', 'Negro Carbono', 'Madone SLR 9', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('6800', 'Azul Marino', 'Canyon Aeroad CF SLX', 'Carretera');
