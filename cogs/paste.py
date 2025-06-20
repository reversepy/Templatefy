# cogs/paste.py

import discord
from discord.ext import commands
from discord import app_commands
from utils.template_utils import load_template

class Paste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="paste", description="Paste a saved template into this server.")
    @app_commands.describe(name="The name of the template to paste")
    async def paste(self, interaction: discord.Interaction, name: str):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild

        if not guild:
            await interaction.followup.send("❌ This command must be used in a server.")
            return

        template = load_template(str(interaction.user.id), name)
        if not template:
            await interaction.followup.send("❌ Template not found.")
            return

        # Create roles
        for role in template.get("roles", []):
            await guild.create_role(
                name=role["name"],
                permissions=discord.Permissions(role["permissions"]),
                colour=discord.Colour(role["color"]),
                mentionable=role["mentionable"],
                hoist=role["hoist"]
            )

        # Create categories and channels
        for category in template.get("categories", []):
            cat = await guild.create_category(name=category["name"])
            for chan in category["channels"]:
                if chan["type"] == "text":
                    await guild.create_text_channel(chan["name"], category=cat)
                elif chan["type"] == "voice":
                    await guild.create_voice_channel(chan["name"], category=cat)

        await interaction.followup.send(f"✅ Template `{name}` pasted into this server!")

async def setup(bot):
    await bot.add_cog(Paste(bot))
