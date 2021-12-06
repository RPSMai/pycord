import discord
from discord.commands import slash_command
from discord.ext import commands, menus


class PageTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.pages = [
            "Page One",
            discord.Embed(title="Page Two"),
            discord.Embed(title="Page Three"),
        ]
        self.pages[1].set_image(url="https://c.tenor.com/pPKOYQpTO8AAAAAM/monkey-developer.gif")
        self.pages[2].add_field(name="Example Field", value="Example Value", inline=False)
        self.pages[2].add_field(name="Another Example Field", value="Another Example Value", inline=False)

    def get_pages(self):
        return self.pages

    @slash_command(name="pagetest")
    async def page(self, ctx):
        await ctx.defer()
        pages = menus.Paginator(pages=self.get_pages(), show_disabled=False, show_indicator=True)
        pages.customize_button("next", button_label=">", button_style=discord.ButtonStyle.green)
        pages.customize_button("prev", button_label="<", button_style=discord.ButtonStyle.green)
        pages.customize_button("first", button_label="<<", button_style=discord.ButtonStyle.blurple)
        pages.customize_button("last", button_label=">>", button_style=discord.ButtonStyle.blurple)
        await pages.send(ctx, ephemeral=False)


def setup(bot):
    bot.add_cog(PageTest(bot))
