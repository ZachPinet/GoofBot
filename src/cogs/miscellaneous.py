import discord
from discord.ext import commands

# This cog groups together miscellaneous commands.
class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # This is the ping command, which returns the bot's latency
    @discord.app_commands.command(name="ping", description="Check GoofBot's latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! ({latency} ms)")

    # This is the mayo command
    @discord.app_commands.command(name="mayo", description="Learn about mayonnaise")
    async def mayo(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Dylan_beast is the Mayo Man! <:mayo:1377043183342587976>")

# Add the MiscCog to the bot.
async def setup(bot):
    await bot.add_cog(MiscCog(bot))
    print("MiscCog loaded successfully.")