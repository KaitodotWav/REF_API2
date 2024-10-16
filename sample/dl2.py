import json, gspread

with open(".cred", 'r', encoding="utf8") as cF:
    cred = json.load(cF)

gc = gspread.oauth(
    credentials_filename='.cred',
    authorized_user_filename='.putin'
)
sh = gc.open("IMPORTANT FILES BATANGAS TRACKER UPDATED")
print(sh.worksheet("FAITH ATTENDANCE Updated").cell(2, 2).value)
