import os, logging, json
log = logging.getLogger("REF SERVER")
log.setLevel("DEBUG")
logHandler = logging.StreamHandler()
logHandler.setLevel("DEBUG")
logFormat = logging.Formatter("%(asctime)s [%(levelname)s] (%(filename)s) - %(message)s")
logHandler.setFormatter(logFormat)
log.addHandler(logHandler)

#carrot
from . import Security
try:
    carrot = Security.Carrot.find(".carrot")
except Exception as e:
    print(e)
    raise Exception("No Carrot to eat")
else: 
    os.environ["carrot"] = carrot.decode()

#compile
potato = {}
with open("Nousagi", "r", encoding="utf8") as Nousagi:
    raw_data = json.load(Nousagi)
for raw_key in raw_data:
    potato[Security.Potato.harvest(raw_key).decode()] = Security.Potato.harvest(raw_data[raw_key]).decode()

#credentials
log.info("importing credentials")
try:
    os.environ["HDB"] = [var for var in open(".db", "r")][0]
except:
    os.environ["HDB"] = potato[".db"]
    log.critical("database file missing switching to potato variables")
finally:
    os.environ["DB_Status"] = "STARTUP"
#os.environ["DB_Status"] = "ERROR"
#vars
log.info("creating global variables")