from API import Security
import json, gspread

with open("Nousagi", "r") as raw:
    raw_data = json.load(raw)

for keys in raw_data:
    dkeys = Security.Potato.harvest(keys.encode())
    ddata = Security.Potato.harvest(raw_data[keys])

    with open(f"{dkeys.decode()}", "w") as file:
        file.write(ddata.decode())

gc = gspread.oauth(
    credentials_filename='.cred',
    authorized_user_filename='.putin'
)

sh = gc.open("IMPORTANT FILES BATANGAS TRACKER UPDATED")
print(sh.worksheet("FAITH ATTENDANCE Updated").cell(2, 2).value)
