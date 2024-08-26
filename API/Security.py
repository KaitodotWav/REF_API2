import discord, os, json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if "auth.json" in os.listdir():
    try:
        with open("auth.json") as J:
            data = json.load(J)
            auth = data["discord"]["token"]
    except Exception as e:
        raise e
else:
    auth = input("unable to find discord token please provide!\ntoken: ")
    client.run(auth)