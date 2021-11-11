from typing import Optional
import utils.database
import disnake
from disnake.ext import commands


class WikiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="create_wiki", aliases=["위키생성", "add_wiki", "생성위키"])
    async def create_wiki(self, ctx: commands.Context, name=None, *, description= None):
        if name!=None and description!=None:
            await utils.database.insert_wiki_data(name, str(ctx.author.id), description)
            await ctx.reply(embed=disnake.Embed(title="성공적으로 위키를 생성했습니다! :white_check_mark:", description=f"위키를 찾고 싶으시다면 ***위키검색 {name}**을 입력해주세요!", color=disnake.Color.random()))
        else:
            await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="양식에 맞게 적어주세요.\n*위키생성 [이름] [설명]", color=disnake.Color.random()))
    
    @commands.command(name="search_wiki", aliases=["검색위키", "위키검색"])
    async def search_wiki(self, ctx: commands.Context, name=None, number:Optional[int]=None):
        if name!=None:
            if number!=None:
                length = await utils.database.get_wiki_data(name)
                if length==[]:await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="찾을 수 없는 위키입니다!"))
                else:
                    try:
                        data = await utils.database.get_wiki_data(name)
                        data = data[number-1]
                        wiki_embed = disnake.Embed(title=data[0], description=data[2], color=disnake.Color.random())
                        wiki_embed.set_footer(text="작성자: " + str(await self.bot.fetch_user(data[1])))
                        await ctx.reply(embed=wiki_embed)
                    except IndexError:
                        await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="위키를 찾을 수 없습니다!"))
            else:
                length = await utils.database.get_wiki_data(name)
                if length==[]: await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="찾을 수 없는 위키입니다!"))
                else:
                    embed_description = "```"
                    loop_num = 0
                    for wiki_data in await utils.database.get_wiki_data(name):
                        loop_num += 1
                        embed_description += f"{wiki_data[0]} : {await self.bot.fetch_user(wiki_data[1])} (*위키검색 {name} {loop_num})\n"
                    embed_description += "```"
                    await ctx.reply(embed=disnake.Embed(title=f"'{name}' 위키 검색", description=embed_description, color=disnake.Color.random()))
        else:
            await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="양식에 맞게 적어주세요.\n*위키검색 [이름]", color=disnake.Color.random()))
    
    @commands.command(name="list_wiki", aliases=["위키목록"])
    async def list_wiki(self, ctx: commands.Context):
        data = await utils.database.get_all_wiki_data()
        wiki_list_embed = disnake.Embed(title="위키 목록", description="```", color=disnake.Color.random())
        for wiki_data in data:
            wiki_list_embed.description += f"{wiki_data[0]} : {await self.bot.fetch_user(wiki_data[1])}\n"
        wiki_list_embed.description += "```"
        await ctx.reply(embed=wiki_list_embed)
    
    @commands.command(name="edit_wiki", aliases=["위키수정", "수정위키", "editwiki"])
    async def edit_wiki(self, ctx: commands.Context, name=None, number:int=None, *, description=None):
        if name!=None and number!=None and description!=None:
            try:
                length = await utils.database.get_wiki_data(name)
                if length==[]:await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="찾을 수 없는 위키입니다!"))
                data = await utils.database.get_wiki_data(name)
                data = data[number-1]
                if data[1]==str(ctx.author.id):
                    await utils.database.edit_wiki_data(description)
                    await ctx.reply(embed=disnake.Embed(title="성공적으로 수정했습니다! :white_check_mark:", description=f"위키를 찾고 싶으시다면 ***위키검색 {name}**을 입력해주세요!", color=disnake.Color.random()))
                else:
                    await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="당신이 작성한 위키가 아닙니다!"))
            except IndexError:
                await ctx.reply(embed=disnake.Embed(title="ERROR :x:", description="위키를 찾을 수 없습니다!"))


def setup(bot):
    bot.add_cog(WikiCog(bot))