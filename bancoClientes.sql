BEGIN TRANSACTION;
CREATE TABLE bancoClientes(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT,
                    telefone TEXT,
                    email TEXT,
                    process TEXT,
                    demanda TEXT,
                    judice TEXT,
                    data TEXT,
                    advers TEXT,
                    valor TEXT,
                    mode TEXT,
                    regist TEXT
            );
INSERT INTO "bancoClientes" VALUES(2,'Maria','98988194046','dfsd@','55555','Diferenças funcionais','1.ª Vara da Fazenda Pública de São Luís','09/09/2022','Estado do Maranhão','1222','normal','');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('bancoClientes',2);
COMMIT;
