import discord

client = discord.Client()
token = "TOKEN"

@client.event 
async def on_ready():
    print("logged in as{0.user}".format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('$hello'):
        await msg.channel.send('haro eburinyan !!')

client.run(token)
