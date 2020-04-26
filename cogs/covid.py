import discord
from discord.ext import commands
from random import randint
from __init__ import postmanRequest


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

        embed_summary_details.set_thumbnail(url="https://www.marketing-schools.org/images/global-marketing.jpg")


        embed_summary_details.add_field(name="New Confirmed", value=f"{summaryData['NewConfirmed']}", inline=False)
        embed_summary_details.add_field(name="Total Confirmed", value=f"{summaryData['TotalConfirmed']}", inline=False)
        embed_summary_details.add_field(name="New Deaths", value=f"{summaryData['NewDeaths']}", inline=False)
        embed_summary_details.add_field(name="Total Deaths", value=f"{summaryData['TotalDeaths']}", inline=False)
        embed_summary_details.add_field(name="New Recovered", value=f"{summaryData['NewRecovered']}", inline=False)
        embed_summary_details.add_field(name="Total Recovered", value=f"{summaryData['TotalRecovered']}", inline=False)

        await ctx.send(embed=embed_summary_details)


def setup(client):
    client.add_cog(covid(client))
