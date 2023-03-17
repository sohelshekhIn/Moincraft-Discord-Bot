import discord
from discord.ext import commands
from python_aternos import Client
from time import sleep

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = "<TOKEN>"
#You discord bot token from developer console
client = discord.Client(intents=discord.Intents.all()) #this maybe optional base on discord library version

@bot.event
async def on_ready():
    print("Bot is up and running")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

        
@bot.command(name="start")
async def start(ctx):
    await ctx.send("Starting server")
    aternos = Client.from_credentials("username", "password")
    servs = aternos.list_servers()
    myserv = servs[0]
    try:
        myserv.start()
    except Exception as e:
        await ctx.send("Server is already running or starting up")
    serverStatus = "offline"
    while serverStatus != "online":
        #logging out and relogging to get updated status of all servers
        aternos.logout()
        aternos = Client.from_credentials("username", "password")
        servs = aternos.list_servers()
        myserv = servs[0]
        # offline, loading, preparing
        if serverStatus != myserv.status:
            serverStatus = myserv.status
            await ctx.send(f"Server is {myserv.status}")
        sleep(10)

@bot.command(name="status")
async def status(ctx):
    aternos = Client.from_credentials('username', 'password')
    servs = aternos.list_servers()
    myserv = servs[0]
    await ctx.send(f"Server is {myserv.status}")

bot.run(token)
