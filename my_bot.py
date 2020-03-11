import discord
from discord.ext.commands import Bot
from time import strftime, sleep
from discord.ext import commands
import asyncio

glo_task = 0

BOT_PREFIX = "!"

TOKEN = 'NDgzNTI4ODA0NjYxMTk4ODY0.DmUxGw.v2gh-ac3vjWvPC18aKcEZjBOyOk'

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(name='reminder', description = "Add a task to complete",pass_context=True)
async def reminder(ctx,*args):
    message = " ".join(args)
    print(ctx.message.content)
    print("ran")
    print ("Today is: " + strftime("%A %B %d, %Y"))
    #split_parts = message.split(' ')
    #print (", ".join(split_parts))
    await client.say(message + " has been added" + "," + ctx.message.author.mention)



    #await client.client.send_message(message.channel,"%s" % (" ".join(args[1:])))

@client.command(pass_context=True)
async def tasks(ctx,user: discord.Member):
    date = strftime("%A %B %d, %Y")
    embed = discord.Embed(title="{}'s tasks".format(user.name), description= "His tasks", color=0xC77EDC)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Today's Date:", value=date, inline=True)
   # embed.add_field(name="Name", value = "hmm", inline= True)
   # embed.add_field(name="Task",value = "hmm", inline= True)
    #embed.set_author(name="mmm")

    embed.set_footer(text= "Due Date: ")
    await client.say(embed=embed)


async def embed(ctx):
    embed = discord.Embed(title="test", description="my name jeff", color=0x00ff00)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)

    await bot.say(embed=embed)

#    await client.say(ctx + "has been added" + "," + context.message.author.mention)

#@client.command(pass_context=True)
#async def complete(ctx, int):

client.run(TOKEN)