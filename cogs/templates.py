# cogs/templates.py

import discord
from discord.ext import commands
from discord import app_commands
from utils.template_utils import list_templates, delete_template

class Templates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="templates", description="List your saved templates.")
    async def templates(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        templates = list_templates(user_id)
        if not templates:
            await interaction.response.send_message("❌ You don't have any saved templates.", ephemeral=True)
            return

        msg = "📁 Your templates:\n" + "\n".join(f"- `{name}`" for name in templates)
        await interaction.response.send_message(msg, ephemeral=True)

    @app_commands.command(name="deletetemplate", description="Delete one of your saved templates.")
    @app_commands.describe(name="The name of the template to delete")
    async def deletetemplate(self, interaction: discord.Interaction, name: str):
        success = delete_template(str(interaction.user.id), name)
        if success:
            await interaction.response.send_message(f"🗑️ Template `{name}` deleted.", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Template not found.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Templates(bot))
