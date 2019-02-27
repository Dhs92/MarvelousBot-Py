from tasks.errorhandle import isadmin
from main import bot


# when command is run, set summoned to true
@bot.command(name='summoned')
@isadmin()
async def summon(ctx):
    await ctx.send('Cancelled Reminder')
    global summoned
    summoned = True

