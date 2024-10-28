import bcrypt, hashlib, base64, json

class Carrot:
    def seed():
        return bcrypt.gensalt()
    
    def plant(seed, farm=".carrot"):
        with open(farm, 'wb') as F: F.write(seed)

    def find(carrot):
        with open(carrot, "rb") as seed:
            return seed.read()

class Potato:
    def plant(data:bytes):
        return base64.b64encode(data)

    def harvest(data:bytes):
        return base64.b64decode(data)

if __name__ == "__main__":
    carrot = Carrot.find(".carrot")
    db = [".cred", ".db", ".putin", "auth.json"]
    dick = {}

    for item in db:
        with open(item, "rb") as file:
            hkey = Potato.plant(item.encode())
            hdata = Potato.plant(file.read())
            dick[hkey.decode()] = hdata.decode()
        with open("Nousagi", 'w') as F:
            json.dump(dick, F, ensure_ascii=False, indent=4)
