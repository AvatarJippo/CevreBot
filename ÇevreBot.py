import discord
from discord.ext import commands
from bot.token import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Benim adım {bot.user}! Ben insaları atıklarını ayrıştırmasına yardımcı olan bir Discord sohbet botuyum!')

@bot.command()
async def Bilgi(ctx):
    await ctx.send(f'Geri dönüştürmeye çalışın. Geri dönüştürülebilir ürünler için bir çöp kutusu ayırın ve dolduğunda geri dönüşüm istasyonuna taşıyın')

bot.run(token)