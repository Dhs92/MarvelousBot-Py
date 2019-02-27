from main import bot
from main import config
import asyncio
from datetime import datetime
import pytz


timezone = pytz.timezone('America/New_York')


async def schedulemessage():
    await bot.wait_until_ready()
    channel = bot.get_channel(int(config.channel))
    bot.fired = False

    while not bot.is_closed():
        bot.fired = False
        now = datetime.now().astimezone(timezone)  # make `now` timezone aware

        if bot.summoned:  # if the summoned command is run, sleep until out of range
            await asyncio.sleep(28800)
            bot.summoned = False
        elif (now.hour == 12) and (now.weekday() == 1 or now.weekday() == 3) and not bot.summoned:
            await channel.send(f'<@{config.adminID}>, <@{config.coAdminID}> Do not forget to summon the guild boss!')
            bot.fired = True

        elif (now.hour == 23) and (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 4) and not bot.summoned:
            await channel.send(f'<@{config.adminID}>, <@{config.coAdminID}> Do not forget to summon the guild boss!')
            bot.fired = True

        if bot.fired:  # if message has fired, sleep until out of range
            await asyncio.sleep(28800)  # 8 hours
            bot.fired = False

        await asyncio.sleep(900)  # 15 minutes


bot.loop.create_task(schedulemessage())