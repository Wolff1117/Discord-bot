import discord, json, os
from random import randint
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import is_owner

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix = "dip!",help_command=None)

qa={}; entries=[]; hahaFunnyImages=[]; hahaFunnyVideos=[]; hahaFunnySounds=[] # defining all variables because debugger is dumb

class event(commands.Cog):
    def __init__(self,client): self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{client.user.name} connected to Discord!\n")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Slave labor'))
        await command.reload(self)
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == client.user: return
        if message.content in qa and not message.author.bot: await message.channel.send(qa[message.content])
        try: await client. process_commands(message)
        except Exception: await message.channel.send('invalid command')
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error): await ctx.send('no')
class command(commands.Cog):
    def __init__(self,client): self.client = client
    @commands.command(name="reload")
    @is_owner()
    async def reload(self,ctx=None):
        globals()['qa'] = json.loads(open('QA.json','r').read())
        globals()['entries'] = json.loads(open('Entries.json','r').read())["Entries"]
        globals()['hahaFunnyImages'] = []; globals()['hahaFunnyVideos'] = []; globals()['hahaFunnySounds'] = []
        for root,files in os.walk(fr"D:\haha funny image"): [hahaFunnyImages.append(f'{root}\\{filename}') for filename in files]  
        for root,files in os.walk(fr"D:\haha funny video"): [hahaFunnyVideos.append(f'{root}\\{filename}') for filename in files]
        for root,files in os.walk(fr"D:\haha funny sound"): [hahaFunnySounds.append(f'{root}\\{filename}') for filename in files]
    @commands.command(name="entry")
    async def entry(self,ctx,index=None):
        if ctx.author.id == 364237299275399168: await ctx.send(entries[2]); return
        try: index = int(index)
        except: await ctx.send(f'Entry must be between 1 and {len(entries)-1}'); return
        if index>len(entries): await ctx.send("Entry Out of Range"); return
        await ctx.send(entries[index])
class help(commands.Cog):
    def __init__(self,client): self.client = client
    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        embed = discord.Embed(title='help',description='dip!help <command> for knowledge',color=0xf40bd5)
        embed.add_field(name='user commands',value='help \nfunny \nentry')
        embed.add_field(name='admin commands',value='reload')
        await ctx.send(embed=embed)
    @help.command(name='reload')
    async def help_reload(self,ctx): await ctx.send(embed=discord.Embed(title='reload',description='Reloads auto-responses',color=0xf40bd5).add_field(name='Syntax',value='dip!reload'))
    @help.command(name='help')
    async def help_help(self,ctx): await ctx.send(embed=discord.Embed(title='help',description='I think you already found out how to use this.',color=0xf40bd5).add_field(name='Syntax',value='dip!help'))
    @help.command(name='funny')
    async def help_funny(self,ctx): await ctx.send(embed=discord.Embed(title='funny',description='Sends a random image from the haha funny image folder.',color=0xf40bd5).add_field(name='Syntax',value='dip!funny'))
    @help.command(name='entry')
    async def help_entry(self,ctx): await ctx.send(embed=discord.Embed(title='entry',description='Displays entry of number given from the Manifest',color=0xf40bd5).add_field(name='Syntax',value=f'dip!entry (1-{len(entries)-1})'))
class funny(commands.Cog):
    def __init__(self,client): self.client = client
    @commands.group(invoke_without_command=True)
    async def funny(self,ctx): await ctx.send(embed=discord.Embed(title='funny',description='dip!funny image\ndip!funny video\ndip!funny sound',color=0xf40bd5))
    @commands.command(name="image")
    async def funnyImage(self,ctx): await ctx.send(file=discord.File(hahaFunnyImages[randint(0,len(hahaFunnyImages))]))
    @commands.command(name="video")
    async def funnyVideo(self,ctx): await ctx.send(file=discord.File(hahaFunnyVideos[randint(0,len(hahaFunnyVideos))]))
    @commands.command(name="sound")
    async def funnySound(self,ctx): await ctx.send(file=discord.File(hahaFunnySounds[randint(0,len(hahaFunnySounds))]))


client.add_cog(command(client))
client.add_cog(event(client))
client.add_cog(funny(client))
client.add_cog(help(client))
client.run(TOKEN)
