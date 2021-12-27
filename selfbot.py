import discord
from discord.ext import commands

# Insert crypto addresses
btc_address = ''
ltc_address = ''
eth_address = ''

# Insert crypto QR code direct URLs (Generate them here: https://www.bitcoinqrcodemaker.com/)
btc_qr = ''
ltc_qr = ''
eth_qr = ''

BOT_PREFIX = "!"
bot = commands.Bot(command_prefix=BOT_PREFIX, case_sensitive=True, self_bot=True)

@bot.event
async def on_ready():
    print("Selfbot Online!")

@bot.command()
async def btc(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Bitcoin Crypto Payment", color=0x505050)
    embed.set_thumbnail(url=btc_qr)
    embed.add_field(name="BTC Address:", value=btc_address, inline=False)
    embed.set_footer(text="NOTICE: At least 1 confirmation should take place for the transaction to complete.")
    await ctx.send(embed=embed)

@bot.command()
async def ltc(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Litecoin Crypto Payment", color=0x505050)
    embed.set_thumbnail(url=ltc_qr)
    embed.add_field(name="LTC Address:", value=ltc_address, inline=False)
    embed.set_footer(text="NOTICE: At least 1 confirmation should take place for the transaction to complete.")
    await ctx.send(embed=embed)

@bot.command()
async def eth(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Litecoin Crypto Payment", color=0x505050)
    embed.set_thumbnail(url=eth_qr)
    embed.add_field(name="ETH Address:", value=eth_address, inline=False)
    embed.set_footer(text="NOTICE: At least 1 confirmation should take place for the transaction to complete.")
    await ctx.send(embed=embed)

@bot.command()
async def rawbtc(ctx):
    await ctx.message.delete()
    await ctx.send(btc_address)

@bot.command()
async def rawltc(ctx):
    await ctx.message.delete()
    await ctx.send(ltc_address)

@bot.command()
async def raweth(ctx):
    await ctx.message.delete()
    await ctx.send(eth_address)

bot.run("NDMwMjcwMjQ0NzYyODEyNDI3.YcjxMw.sBir0DRCXhm-LSWkhvGGCpEJjTE", bot=False)