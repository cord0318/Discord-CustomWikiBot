import disnake, config, os

from disnake.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="load", aliases=["로드"])
    async def load(self, ctx: commands.Context, path=None):
        if ctx.author.id in config.OWNER_ID:
            if path == "*" or path == "." or path == None:
                msg = await ctx.send(f"**모든 extensions**을 로드 하는중...")
                for e in [f for f in os.listdir("src/extensions") if f.endswith('py')]:
                    self.bot.load_extension(f'extensions.{e.replace(".py", "")}')
            else:
                msg = await ctx.send(f"`extensions`의 **{path}**를 로드 하는중...")
                self.bot.load_extension(f"extensions.{path}")
            await msg.edit(content=":white_check_mark: **성공적으로 모듈을 로드 하였습니다!**")
        else:
            await ctx.send(":x: 당신은 이 봇의 **OWNER**가 아닙니다!")

    @commands.command(name="reload", aliases=["리로드", "Reload", "flfhem"])
    async def reload(self, ctx: commands.Context, path=None) -> None:
        if ctx.author.id in config.OWNER_ID:
            if path == "*" or path == "." or path == None:
                msg = await ctx.send(f"**모든 extensions**을 리로드 하는중...")
                for e in [f for f in os.listdir("src/extensions") if f.endswith('py')]:
                    self.bot.reload_extension(f'extensions.{e.replace(".py", "")}')
            else:
                msg = await ctx.send(f"`extensions`의 **{path}**를 리로드 하는중...")
                self.bot.reload_extension(f"extensions.{path}")
            await msg.edit(content=":white_check_mark: **성공적으로 모듈을 리로드 하였습니다!**")
        else:
            await ctx.send(":x: 당신은 이 봇의 **OWNER**가 아닙니다!")  

    
    @commands.command(name="list_extension", aliases=["기능리스트", "list"])
    async def list_extension(self, ctx: commands.Context):
        if ctx.author.id in config.OWNER_ID:
            EXTENSION_LIST=[]
            for e in [f for f in os.listdir("src/extensions") if f.endswith('py')]:
                EXTENSION_LIST.append(f'extensions.{e.replace(".py", "")}')
            embed = disnake.Embed(title="[ EXTENSION LIST ]")
            embed.description = "***" + ", ".join(EXTENSION_LIST).replace("extensions.", "") + "***"
            await ctx.send(embed=embed)
            
    @commands.command(name="help", aliases=["도움말", "도움", "헬프"])
    async def help(self, ctx: commands.Context):
        help_embed = disnake.Embed(title="[ 도움말 ]", color=disnake.Color.random())
        help_embed.description = "*위키생성 [이름] [설명] - 위키를 생성합니다. (create_wiki, add_wiki, 생성위키)\n*위키검색 [이름] [번호(선택)] - 위키를 검색합니다. (search_wiki, 검색위키)\n*help - 도움말을 봅니다.\n*위키목록 - 위키의 목록을 봅니다.\n*위키수정 [이름] [번호] [수정할 설명] - 위키를 수정합니다. (위키 작성자만 가능)"
        await ctx.reply(embed=help_embed)
def setup(bot):
    bot.add_cog(AdminCog(bot))