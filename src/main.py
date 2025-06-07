import discord
from discord.ext import commands
import asyncio

import settings


# This is GoofBot's main entry point.
async def main():
    intents = discord.Intents.all()
    
    bot = commands.Bot(command_prefix='g!', intents=intents)

    # Load the cogs
    await bot.load_extension('cogs.miscellaneous')
    
    # This brings the bot online when main is run
    @bot.event
    async def on_ready():
        print("Goofbot is online")

        # Sync slash commands
        try:
            guild = discord.Object(id=settings.GUILD_ID)
            synced = await bot.tree.sync(guild=guild)
            print(f"Synced {len(synced)} command(s) to guild")
        except Exception as e:
            print(f"Failed to sync commands: {e}")
    
    # Start the bot
    await bot.start(settings.TOKEN)


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())