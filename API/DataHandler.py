import psycopg2 as psycho
import psycopg2.sql as sql
import logging, os, binascii
from . import Security

log = logging.getLogger("REF SERVER")
DB_KEYS = os.environ["HDB"]
TABLES = ["IDS", "Students", "Statements", "Sessions"]

class DB():
    def __init__(self):
        if os.environ["DB_Status"] == "STARTUP":
            log.info("connection test on database")
            try:
                tdb = psycho.connect(DB_KEYS, sslmode="require")
                tdb.close()
                log.info("database connection success!")
            except Exception as e:
                log.critical(f"SKILL ISSUE! {e}")
            os.environ["DB_Status"] = "SETUP"
            self.setup()


    def execute(self, command=None):
        if command is None: return 0
        with psycho.connect(DB_KEYS, sslmode="require") as DB:
            with DB.cursor() as console:
                if type(command) == str:
                    console.execute(command)
                    if "select" in command.lower(): return console.fetchall()
                    else:
                        return None
                
                elif type(command) == list:
                    results = []
                    for cl in command:
                        console.execute(cl)
                        if "select" in cl.lower():
                            results.append(console)
                        else: return None
                    return results
                
    def setup(self):
        log.info("checking tables")
        self.execute("DROP TABLE Auth")
        try:
            self.execute("SELECT * FROM Auth")
            log.info("Auth table exist")
        except psycho.errors.UndefinedTable:
            log.warning("Auth table doesnt exist. creating table")
            self.execute(
                """
                CREATE TABLE Auth (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    username VARCHAR(100) NOT NULL,
                    password VARCHAR NOT NULL,
                    authlevel INT NOT NULL,
                    accesstype INT NOT NULL
                )
                """
            )
        #superusr
        try: c = self.execute("SELECT * FROM Auth WHERE NAME = 'SUSER'")
        except Exception as e:
            usr = "SUSER"
            pwd = Security.bcrypt.hashpw("REFSuperUser".encode(), os.environ["carrot"].encode())
            #self.execute(f"INSERT INTO Auth (name, username, password, authlevel, accesstype) VALUES ({usr}, {usr}, {pwd}, 0, 0)")
            print(type(e), e)
        else:
            if len(c) != 0: return
            else:
                usr = "SUSER"
                pwd = Security.bcrypt.hashpw("REFSuperUser".encode(), os.environ["carrot"].encode())
                print(binascii.hexlify(pwd).decode('ascii'))
                self.execute(f"INSERT INTO Auth (name, username, password, authlevel, accesstype) VALUES ('{usr}', '{usr}', '{binascii.hexlify(pwd).decode('ascii')}', 0, 0)")