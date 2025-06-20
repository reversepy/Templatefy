# cogs/copy.py

import discord
from discord.ext import commands
from discord import app_commands
from utils.template_utils import save_template

class Copy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="copy", description="Save the current server’s structure as a template.")
    @app_commands.describe(name="The name for this template")
    async def copy(self, interaction: discord.Interaction, name: str):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild

        if not guild:
            await interaction.followup.send("❌ This command can only be used in a server.")
            return

        data = {
            "name": guild.name,
            "roles": [],
            "categories": []
        }

        # Copy roles (excluding @everyone)
        for role in guild.roles[::-1]:
            if role.name != "@everyone":
                data["roles"].append({
                    "name": role.name,
                    "color": role.color.value,
                    "permissions": role.permissions.value,
                    "mentionable": role.mentionable,
                    "hoist": role.hoist
                })

        # Copy channel structure
        for category in guild.categories:
            cat_data = {
                "name": category.name,
                "channels": []
            }
            for channel in category.channels:
                if isinstance(channel, discord.TextChannel):
                    cat_data["channels"].append({
                        "name": channel.name,
                        "type": "text"
                    })
                elif isinstance(channel, discord.VoiceChannel):
                    cat_data["channels"].append({
                        "name": channel.name,
                        "type": "voice"
                    })
            data["categories"].append(cat_data)

        save_template(str(interaction.user.id), name, data)
        await interaction.followup.send(f"✅ Template `{name}` saved!")

async def setup(bot):
    await bot.add_cog(Copy(bot))
