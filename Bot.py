import discord, json, os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix = "dip!")
client.remove_command('help')
with open('QA.json','r') as file:
    qa = json.loads(file.read())


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await autoResponse(message)
    await client.process_commands(message)
async def autoResponse(ctx):
    response = ""
    if ctx.author.bot: return
    if ctx.content in qa: await ctx.channel.send(qa[ctx.content])


@client.event
async def on_ready():
    print(f"{client.user.name} connected to Discord!\n")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Hentai'))

@client.command(name = "test")
async def test(ctx):
    await ctx.send(embed = discord.Embed(title = "Bot Commands", description = "WIP", color = 0xf40bd5))

@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title='help',description='dip!help <command> for knowledge',color=0xf40bd5)
    embed.add_field(name='user commands',value='help')
    embed.add_field(name='admin commands',value='reload')
    await ctx.send(embed=embed)

@help.command(name='reload')
async def help_reload(ctx): await ctx.send(embed=discord.Embed(title='reload',description='placeholder_text',color=0xf40bd5).add_field(name='Syntax',value='dip!reload'))

@help.command(name='help')
async def help_reload(ctx): await ctx.send(embed=discord.Embed(title='help',description='I think you already found out how to use this.',color=0xf40bd5).add_field(name='Syntax',value='dip!help'))

@client.command(name = "reload")
async def reload(ctx):
    global qa
    with open('QA.json','r') as file:
        qa = json.loads(file.read())
    await ctx.send("done")
    
client.run(TOKEN)
