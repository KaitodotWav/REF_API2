import os, logging
log = logging.getLogger("REF SERVER")
log.setLevel("DEBUG")
logHandler = logging.StreamHandler()
logHandler.setLevel("DEBUG")
logFormat = logging.Formatter("%(asctime)s [%(levelname)s] (%(filename)s) - %(message)s")
logHandler.setFormatter(logFormat)
log.addHandler(logHandler)


#credentials
log.info("importing credentials")
try:
    print(os.environ["HDB"])
except:
    os.environ["HDB"] = [var for var in open(".db", "r")][0]

#vars
log.info("creating global variables")
os.environ["DB_Status"] = "STARTUP"