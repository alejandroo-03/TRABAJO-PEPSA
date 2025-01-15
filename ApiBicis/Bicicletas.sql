CREATE DATABASE IF NOT EXISTS DEATHBIKES;
USE DEATHBIKES;

CREATE TABLE IF NOT EXISTS bicicletas (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    precio DECIMAL(8,2) NOT NULL,
    color VARCHAR(255) NOT NULL,
    modelo VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS usuarios (
    nombre VARCHAR(255) NOT NULL,
    clave VARCHAR(18) NOT NULL
);

-- Agregamos inserts
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('6500', 'Satin Cooper/Smoke', 'Roubaix SL8 Expert', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('7500', 'Blanco Mate', 'Venge Pro', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('8200', 'Rojo Brillante', 'Tarmac SL7', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('9200', 'Negro Carbono', 'Madone SLR 9', 'Carretera');
INSERT INTO bicicletas (precio, color, modelo, tipo) VALUES ('6800', 'Azul Marino', 'Canyon Aeroad CF SLX', 'Carretera');


INSERT INTO usuarios (nombre, clave) VALUES ('Alejandro', '1234');
INSERT INTO usuarios (nombre, clave) VALUES ('Ivan', '1234');
INSERT INTO usuarios (nombre, clave) VALUES ('Fernando', 'Clave$1');
INSERT INTO usuarios (nombre, clave) VALUES ('Alberto', '1234');
INSERT INTO usuarios (nombre, clave) VALUES ('Invitado', '1234');
