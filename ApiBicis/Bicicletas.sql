CREATE DATABASE IF NOT EXISTS DEATHBIKES;
USE DEATHBIKES;

CREATE TABLE IF NOT EXISTS bicicletas (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(8,2) NOT NULL,
    foto VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS usuarios (
    nombre VARCHAR(255) NOT NULL,
    clave VARCHAR(18) NOT NULL
    
);

-- Agregamos inserts
INSERT INTO bicicletas (nombre, descripcion, precio, foto)
VALUES 
    ('Bici de montaña', 'Una bici para senderismo en montaña', 250.00, 'imagen1'),
    ('Bici de carretera', 'Bici ligera para ciclismo en carretera', 180.00, 'bici2.png'),
    ('Bici urbana', 'Bici para uso diario en la ciudad', 120.00, 'imagen3'),
    ('Bici eléctrica', 'Bici con motor eléctrico para facilitar el pedaleo', 600.00, 'imagen4'),
    ('Bici plegable', 'Bici compacta que se puede plegar para facilitar su transporte', 150.00, 'imagen5');



INSERT INTO usuarios (nombre, clave) VALUES ('Alejandro', '1234');
INSERT INTO usuarios (nombre, clave) VALUES ('Ivan', '1234');
INSERT INTO usuarios (nombre, clave) VALUES ('Fernando', 'Clave$1');
INSERT INTO usuarios (nombre, clave) VALUES ('Alberto', '1234');
INSERT INTO usuarios (nombre, clave) VALUES ('Invitado', '1234');
