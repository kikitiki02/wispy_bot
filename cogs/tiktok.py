import discord
from discord.ext import commands
import yt_dlp
import os


class TikTokCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if "tiktok.com" in message.content:
            await message.channel.send("Getting the tiktok for you lazy :/...")

            try:
                ydl_opts = {
                    "outtmpl": "video.mp4",
                    "format": "mp4",
                    "quiet": True
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([message.content])

                await message.channel.send(
                    file=discord.File("video.mp4")
                )

                os.remove("video.mp4")

            except Exception as e:
                await message.channel.send("uhmmm this won't work bub.")
                print(e)


async def setup(bot):
    await bot.add_cog(TikTokCog(bot))