from config.conf import Config
import discord
from bot import bot
from discord.ext import commands
from commands import summon
from commands import quitbot
import logging


# globals
##########
logging.basicConfig(level=logging.INFO)

config = Config()

bot.summoned = False
###########


@bot.event
async def on_ready():
    print('Starting up....')
    game = discord.Game(name='Grand Chase Dimensional Chasers')
    await bot.change_presence(activity=game)


@summon.error
async def summonerror(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('You do not have permission to run this command!')


@quitbot.error
async def quiterror(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('You do not have permission to run this command!')

# @bot.command()
# @isOwner()
# async def reload(ctx):
#     if isOwner():
#         await ctx.send('Restarting...')
#     await bot.close()
#     await bot.run(config.token)


bot.run(config.token)
