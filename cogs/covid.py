import discord
from discord.ext import commands
from random import randint
from __init__ import postmanRequest
import pandas as pd
from matplotlib import pyplot
from datetime import datetime


class covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Bot greet
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online!")

    # Summary of confirmed cases
    @commands.command()
    async def summary(self, ctx):
        summaryData = postmanRequest(f"/summary")['Global']

        embed_summary_details = discord.Embed(colour=randint(0, 0xffffff))

        embed_summary_details.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/globe-512.png")


        embed_summary_details.add_field(name="New Confirmed", value=f"{summaryData['NewConfirmed']}", inline=False)
        embed_summary_details.add_field(name="Total Confirmed", value=f"{summaryData['TotalConfirmed']}", inline=False)
        embed_summary_details.add_field(name="New Deaths", value=f"{summaryData['NewDeaths']}", inline=False)
        embed_summary_details.add_field(name="Total Deaths", value=f"{summaryData['TotalDeaths']}", inline=False)
        embed_summary_details.add_field(name="New Recovered", value=f"{summaryData['NewRecovered']}", inline=False)
        embed_summary_details.add_field(name="Total Recovered", value=f"{summaryData['TotalRecovered']}", inline=False)

        await ctx.send(embed=embed_summary_details)


    # Death count graph for Germnay
    @commands.command()
    async def germany(self, ctx):
        data = postmanRequest('dayone/country/Germany')

        dataSet = [(datetime.strptime(i['Date'], "%Y-%m-%dT%H:%M:%SZ").strftime("%b"), j['Deaths']) for i, j in
                   zip(data, data)]

        df = pd.DataFrame(dataSet)

        df.plot(x=0, y=1)

        pyplot.title('Showing Deaths in Germany')
        pyplot.xlabel('Months')
        pyplot.ylabel('Number of Deaths')

        pyplot.savefig('./image/image.png')

        await ctx.send(file=discord.File("./image/image.png"))


def setup(client):
    client.add_cog(covid(client))