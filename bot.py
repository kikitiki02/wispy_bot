import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

TOKEN= os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 pong!! 💕")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if "hi" in message.content.lower().split():
        await message.channel.send("You're mad loud gang")
    if "sad" in message.content.lower():
        await message.channel.send("aw nooo 🥺 I'm here for you 🤍....nah im just playin. Get it together")
    if "lipi" in message.content.lower():
        await message.channel.send("Lipi? He's stinky.")
    if "cod" in message.content.lower().split():
        await message.channel.send("PEEE YUUUU ONION BOY")
    if "rl" in message.content.lower().split():
        await message.channel.send("are you serious....?")
    if "novo" in message.content.lower():
        await message.channel.send("OI we SUCKIN WEENIEs MATE")
    if "allie" in message.content.lower():
        await message.channel.send("HEY QUEEN LUV YA")
    if "kiki" in message.content.lower():
        await message.channel.send("Kiki is the most amazing person ever and she's my mutha")
        
    await bot.process_commands(message)


async def setup_hook():
    await bot.load_extension("cogs.tiktok")

bot.setup_hook = setup_hook

bot.run(TOKEN)