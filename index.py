from discord_easy_commands import EasyBot
import discord
import pyjokes

tokens = "MTE0MTUyOTU1MDkzNzkzMTgzOQ.Grjq25.Vma8KXOHdVhKjwHgWgN5gMtgVmmd1_Iruhojqw"
intents = discord.Intents.all()
jokes = pyjokes.get_jokes(language="es", category="all")
bot = EasyBot(intents=intents)
bot.setCommand(
    "!tiktok", "https://www.tiktok.com/@chrisjonez/video/6982992929472154885"
)
bot.setCommand("!chiste", jokes)
bot.run(tokens)
