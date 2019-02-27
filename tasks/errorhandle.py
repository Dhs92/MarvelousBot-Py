from discord.ext import commands
from main import config


# check if command was run by me :)
def isowner() -> bool:
    async def predicate(ctx):
        return ctx.author.id == 158161676749766656
    return commands.check(predicate)


def isadmin() -> bool:
    async def predicate2(ctx):
        return ctx.author.id == int(config.adminID) or ctx.author.id == int(config.coAdminID)
    return commands.check(predicate2)