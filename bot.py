import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="HIC")

@bot.event
async def on_ready():
    print(" Watson is online ")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(837629228215566356)
    await channel.send(f"༺ཌༀൢ {member}want Waston ! ൢༀད༻")
 
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(837629228215566356)
    await channel.send(f"༺ཌༀൢ {member}betray Watson ! ൢༀད༻")

bot.run("ODQ3MDkwNzU1NzAwNjU0MDgw.YK5Avg.yej9J5XN0xJ9FGkc7B5kXknpOic")

