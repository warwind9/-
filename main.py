import discord
from discord.ext import commands
import hcskr



token = "" # 당신의 봇의 token
prefix = "!" # 당신이 원하는 봇의 접두사 (기본값 '!')


app = commands.Bot(command_prefix=prefix) # 바꾸지 마세요


@app.event # 봇 시작 구문
async def on_ready():
    print("Start Discord Bot")
    print(app.user.name)
    print(app.user.id)
    print(app.user)
    print(f"Prefix: {app.command_prefix}")
    await app.change_presence(status = discord.Status.online)
    print("==================")



@app.command() # 디스코드 봇 구문
async def 자가진단(ctx, name = None, celebrate = None, area = None, school = None, school_type = None, password = None):
    if ctx.channel.type == discord.ChannelType.private:
        if name != None:
            if celebrate != None:
                if area != None:
                    if school != None:
                        if school_type != None:
                            if password != None:
                                await hcskr.asyncSelfCheck(name, celebrate, area, school, school_type, password)
                                result = await hcskr.asyncSelfCheck(name, celebrate, area, school, school_type, password)
                                msg = result["message"]
                                code = result["code"]
                                if result["error"] == True:
                                    embed = discord.Embed(title="Error", description=f"**Error Code: `{code}`\nError Message: `{msg}`**", colour=discord.Colour.red())
                                    await ctx.send(embed=embed)
                                else:
                                    embed = discord.Embed(title="Success!", description=f"**{msg}**", colour=discord.Colour.green())
                                    await ctx.send(embed=embed)  
                            else:
                                await ctx.send(f"자가진단 비밀번호를 적어주세요!\n(ex: 1234")
                        else:
                            await ctx.send("'유치원', '유','유치'\n'초등학교', '초','초등'\n'중학교', '중','중등'\n'고등학교', '고','고등'\n'특수학교', '특','특수','특별'중 해당되는 것을 적어주세요!")
                    else:
                        await ctx.send("학교를 적어주세요!")
                else:
                    await ctx.send("당신이 사는 지역을 적어주세요!")
            else:
                await ctx.send("당신의 생일 6자리를 적어주세요!\n(ex:2007-12/1 -> 071201")
        else:
            embed = discord.Embed(title="Help", description=f"**{app.command_prefix}자가진단 [이름] [생일6자리] [지역] [학교] [학교종류] [비밀번호]**", colour=discord.Colour.red())
            await ctx.send(embed=embed) 
    else:
        await ctx.send("이 명령어는 봇의 DM에서만 사용 가능합니다!")