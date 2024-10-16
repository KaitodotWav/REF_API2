import psycopg2 as psycho
import psycopg2.sql as sql
import logging, os

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
                if type(command) == str: return console.execute(command)
                
                elif type(command) == list:
                    results = []
                    for cl in command: results.append(console.execute(cl))
                    return results
                
    def setup(self):
        log.info("checking tables")
        try:
            self.execute("SELECT * FROM Auth")
            log.info("Auth table exist")
        except psycho.errors.UndefinedTable:
            log.warning("Auth table doest exist. creating table")
            self.execute(
                """
                CREATE TABLE Auth (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    username VARCHAR(100) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    authlevel INT NOT NULL,
                    accesstype INT NOT NULL
                )
                """
            )