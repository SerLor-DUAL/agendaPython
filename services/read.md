Habrá que crear unas tablas nuevas en la BD de la empresa, para hacer las pruebas.


Serán la de usuario y eventos, que seguirán estas estructuras en Integra

**USERS_NUE**
nue_id                  INT PRIMARY KEY,
nue_nickname            VARCHAR(100) NOT NULL DEFAULT '',
nue_hashedPassword      VARCHAR(500),
nue_recordCreation      TIMESTAMP,  
nue_recordModification  TIMESTAMP      -- Este es el que autogenera INTEGRA, habría que borrar recordUser, pues no tiene sentido

**EVENTS_NEV**
nev_id                  INT PRIMARY KEY,
nev_title               VARCHAR(100) NOT NULL DEFAULT '',
nev_description         VARCHAR(500),
nev_startTime           TIMESTAMP,
nev_endTime             TIMESTAMP,
nev_recordCreation      TIMESTAMP,
nev_recordModification  TIMESTAMP,   -- Este es el que autogenera INTEGRA, habría que borrar recordUser, pues no tiene sentido
nue_nev_n_fk            INT FOREIGN KEY -- Con este ligaremos los eventos a su usuario


Crearemos un link entre USERS_NUE y EVENTS_NEV en el que la relación será (0,n) a (0,1) si se borra un usuario se borran sus eventos, si se modifica el usuario, los eventos vinculados a este también.