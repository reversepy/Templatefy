# bot.py

import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")  # Optional: for syncing commands quickly during dev

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = False
intents.members = True

class Templafy(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=os.getenv("APPLICATION_ID")
        )
        self.initial_extensions = [
            "cogs.copy",
            "cogs.paste",
            "cogs.templates"
        ]

    async def setup_hook(self):
        # Load extensions
        for ext in self.initial_extensions:
            await self.load_extension(ext)

        # Sync commands
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            print(f"Commands synced to guild: {GUILD_ID}")
        else:
            await self.tree.sync()
            print("Commands synced globally")

    async def on_ready(self):
        print(f"✅ Logged in as {self.user} (ID: {self.user.id})")
        print("Templafy is ready!")

bot = Templafy()
bot.run(TOKEN)
