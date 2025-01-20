-- Crear base de datos
CREATE DATABASE IF NOT EXISTS 4thewords_prueba_Darvin_Gutierrez;
USE 4thewords_prueba_Darvin_Gutierrez;

-- Crear tabla para las leyendas
CREATE TABLE leyendas (
    id INT AUTO_INCREMENT PRIMARY KEY,              -- Identificador único
    nombre VARCHAR(255) NOT NULL,                  -- Nombre de la leyenda
    descripcion TEXT NOT NULL,                     -- Descripción detallada
    fecha_leyenda DATE NOT NULL,                   -- Fecha asociada a la leyenda
    provincia VARCHAR(100) NOT NULL,               -- Provincia
    canton VARCHAR(100) NOT NULL,                  -- Cantón
    distrito VARCHAR(100) NOT NULL,                -- Distrito
    imagen_url VARCHAR(255),                       -- URL o imagen asociada
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha de creación del registro

);

-- Insertar datos en la tabla leyendas
INSERT INTO leyendas (nombre, descripcion, fecha_leyenda, provincia, canton, distrito, imagen_url)
VALUES
('La Tulevieja', 
 'Leyenda que cuenta la historia de una mujer que deambula en busca de su hijo perdido.', 
 '1850-01-01', 
 'San José', 
 'San José', 
 'Carmen', 
 'https://grupoinframundo.com/wp-content/uploads/2024/10/462636997_3906692902907343_1056429451411947446_n.jpg'),
('El Cadejo', 
 'Un perro fantasma que aparece para proteger o castigar a los viajeros nocturnos.', 
 '1900-01-01', 
 'Cartago', 
 'Cartago', 
 'Oriental', 
 'https://cdn.sanjosecostarica.org/wp-content/uploads/2020/07/El-Cadejo-485x485.jpg'),
('La Segua', 
 'Leyenda de una mujer que se transforma en un monstruo para castigar a los hombres infieles.', 
 '1750-01-01', 
 'Guanacaste', 
 'Liberia', 
 'Liberia', 
 'https://images.podcastpage.io/fetch/https%3A%2F%2Fsites.podcastpage.io%2F65e203f2dcfc57fb25f26d66%2Fmedia%2F467321e66087335dd564.jpg'),
('El Padre Sin Cabeza', 
 'Leyenda sobre un sacerdote decapitado que aparece en los alrededores de iglesias antiguas.', 
 '1800-01-01', 
 'Alajuela', 
 'Alajuela', 
 'Central', 
 'https://pbs.twimg.com/media/EgekiP1XsAIqK3k.jpg'),
('La Llorona', 
 'Una madre que llora eternamente por sus hijos perdidos cerca de los ríos.', 
 '1600-01-01', 
 'Heredia', 
 'Heredia', 
 'San Francisco', 
 'https://www.muyinteresante.com.mx/wp-content/uploads/sites/6/2024/10/La-Llorona.png'),
('Los Duendes', 
 'Leyenda que los duendes son unos hombrecitos muy pequeños y de orejas puntiagudas.', 
 '1700-01-01', 
 'Guanacaste', 
 'Santa Cruz', 
 'Paso Hondo', 
 'https://www.castellariegos.com/images/easyblog_articles/254/duende-portada.jpg'),
('La Mona', 
 'La Mona es una criatura de la leyenda guanacasteca que se caracteriza por tener aspecto de simio, un grito aterrador y la capacidad de desplazarse rápidamente por los árboles.', 
 '1850-01-01', 
 'Guanacaste', 
 'Nicoya', 
 'Nicoya', 
 'https://sicultura-live.s3.amazonaws.com/public/media/la_mona_tasa.jpg'),
('La bruja de Escazu', 
 'Cuenta la leyenda que esta bruja era negrita y una de las últimas brujas del pueblo más renombradas, que habitaba al norte de la Iglesia del centro de Escazú.', 
 '1900-01-01', 
 'San José', 
 'Escazú', 
 'San Rafael', 
 'https://mexicotravelchannel.com.mx/wp-content/uploads/2021/07/xochimilco-bruja-de-xaltocan-leyenda.jpg'),
('Carreta Sin Bueyes', 
 'La carreta sin bueyes es una leyenda costarricense que narra la aparición de un espectro nocturno en forma de carreta que deambula por las calles de un pueblo o ciudad.', 
 '1700-01-01', 
 'Guanacaste', 
 'Nicoya', 
 'Nicoya', 
 'https://poasrentacar.com/blog/wp-content/uploads/2017/09/oxlesscart940x1126-855x1024.png'),
('El Viejo del Monte', 
 'Leyenda de un anciano protector de los bosques que castiga a quienes los dañan.', 
 '1850-01-01', 
 'San José', 
 'Escazú', 
 'San Rafael', 
 'https://www.periodicomensaje.com/images/2020/Viejo_del_Monte.jpg');

