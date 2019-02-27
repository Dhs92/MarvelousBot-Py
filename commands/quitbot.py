from tasks import errorhandle
import main


# close the bot safely
@main.bot.command()
@errorhandle.isowner()
async def quitbot(ctx):
    await ctx.send('Closing...')
    await main.bot.close()
