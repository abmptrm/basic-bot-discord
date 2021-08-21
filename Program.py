import discord

client = discord.Client()
token = "ODc4NTM4Nzc2NTY0MDg4ODMy.YSCo_g.DOR_CUYH0jgIw1T-APff1XsCOQc"

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