CREATE DATABASE IF NOT EXISTS DEATHBIKES;
CREATE USER 'user'@'%' IDENTIFIED BY 'userpw';
GRANT ALL PRIVILEGES ON DEATHBIKES.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE DEATHBIKES;

CREATE TABLE IF NOT EXISTS bicicletas (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(8,2) NOT NULL,
    foto VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS usuarios (
    nombre VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(254) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    fechaUltimoAcceso DATE,
    fechaBloqueo DATE,
    numeroAccesosErroneo INTEGER,
    debeCambiarClave BOOLEAN
    
);

-- Agregamos inserts
INSERT INTO bicicletas (nombre, descripcion, precio, foto)
VALUES 
    ('Bici de montaña', 'Una bici para senderismo en montaña', 250.00, 'imagen1'),
    ('Bici de carretera', 'Bici ligera para ciclismo en carretera', 180.00, 'bici2.png'),
    ('Bici urbana', 'Bici para uso diario en la ciudad', 120.00, 'imagen3'),
    ('Bici eléctrica', 'Bici con motor eléctrico para facilitar el pedaleo', 600.00, 'imagen4'),
    ('Bici plegable', 'Bici compacta que se puede plegar para facilitar su transporte', 150.00, 'imagen5');



--INSERT INTO usuarios (nombre, clave) VALUES ('Alejandro', '1234');
--INSERT INTO usuarios (nombre, clave) VALUES ('Ivan', '1234');
--INSERT INTO usuarios (nombre, clave) VALUES ('Fernando', 'Clave$1');
--INSERT INTO usuarios (nombre, clave) VALUES ('Alberto', '1234');
--INSERT INTO usuarios (nombre, clave) VALUES ('Invitado', '1234');


--INSERT INTO `usuarios` (`usuario`,`clave`,`perfil`,`estado`, `correo`, `numeroAccesosErroneo`,`fechaUltimoAcceso`)VALUES ('admin', 'activo','root@bikes.es', 0, '2022-03-01 00:00')