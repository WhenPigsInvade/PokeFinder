import find
import urllib.request
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('bot online')
    print(bot.user.name)

@bot.event
async def on_message(message):
    if message.author.id == 716390085896962058:
##        print(message.message.content())

        embeds = message.embeds # return list of embeds
##        for embed in embeds:
##            print(embed.to_dict()) # it's content of embed in dict

        if len(embeds) > 0:
            embed = embeds[0]
            embed = embed.to_dict()
        else:
            return

        if embed is not None and embed.get("image") is not None and embed.get("description") is not None and embed.get("description")== 'Guess the pokémon and type `p!catch <pokémon>` to catch it!':
            url = embed.get("image").get("url")

            print(url)

            # Adding information about user agent
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)

            # setting filename and image URL

            # calling urlretrieve function to get resource
            urllib.request.urlretrieve(url, "pokemon.jpg")

            
            
            results = find.find("pokemon.jpg", 0.97)

            txt = ""
            for poke in zip([1, 2, 3], results):
                txt = txt + str(poke)

            await message.reply(str)

    if message.author.id == 851869159121616960:

        embeds = message.embeds # return list of embeds
##        for embed in embeds:
##            print(embed.to_dict()) # it's content of embed in dict

        embed = embeds[0]
        embed = embed.to_dict()
        print(embed)
        print(embed.get("title"))


with open("token.txt", "r") as file:
    token = file.read().splitlines()[0].strip()
bot.run(token)
