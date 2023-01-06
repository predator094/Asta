import asyncio
from prettytable import PrettyTable
import discord
from discord.ext import commands
from discord.ext import tasks
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import re
import datetime
import os
import xlsxwriter
from myfunc import *
from vggc import *
from keep_alive import keep_alive

keep_alive()
intents = discord.Intents.all()
TOKEN = os.environ['TOKEN']
prefix = "="
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix),
                   strip_after_prefix=True,
                   intents=intents)
#Global variables:-
red = int("ff0000", 16)
ftl=[]
@tasks.loop(seconds=1)
async def pot():
  poi= datetime.datetime.now() + datetime.timedelta(hours=5,minutes=30)
  a=poi.strftime("%X")
  print(a)
  if a in ftl:
    await m()
async def m():
  a=bot.get_user(747201484701040758)
  await a.send("chal gya me betuichod")
@bot.command()
async def d2m(ctx,*,b):
    a=re.compile("\d{18}")
    list=a.findall(b)
    c=len(list)
    i=0
    list1=[]
    a1="<@"
    a2=">"
    while i < c:
        a=a1 + list[i] + a2
        list1.append(a)
        i+=1
    list2= "\n".join(list1)
    await ctx.send("`{}`".format(list2))


@bot.event
async def on_message(message):
  if message.guild==None and message.author!=bot.user:
    a=message.content
    b=message.author
    ctx=bot.get_channel(897997299031109665)
    await cembed(ctx,red,f"**ID:- {message.author.id}\nContent :-\n{a}**",message.author)
  await bot.process_commands(message)

@bot.event
async def on_ready():
    game = discord.Game("in the Clover Kingdom()".format(prefix))
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print("Bot is ready")
    pot.start()


@bot.command()
async def utbc(ctx,*,a):
    b=re.compile("Team .*(name -|Name -).*")
    c=b.findall(a)
    i=0
    while i < len(c):
        a1=c[i]
        if "Team Name -" in a1:
            a2=a1.replace("Team Name -","")
            c[i]=a2
            i+=1
        if "Team name -" in a1:
            a2=a1.replace("Team name -","")
            c[i]=a2
            i+=1
    a1 = len(c)
    c1=[] 
    i=0
    while i <len(c):
        a=f"SLOT {i+3} ➠ {c[i]}"
        c1.append(a)
        i+=1
    c2="\n".join(c1)
    await ctx.send(f"""`**╔───────── ¤ ◎ ◎ ¤ ─────────╗
            FAN CUP BGMI
╚───────── ¤ ◎ ◎ ¤ ─────────╝
           GROUP SLOT LIST \n\n{c2}\n**`""")
        
        
  

@bot.command()
async def qui(ctx,*,b):
    if b.lower()=="file":
      if ctx.message.attachments!=[]:
        await ctx.send("file nhi hai ")
        await ctx.message.attachments[0].save("rcf.txt")
        f1=open("rcf.txt","r")
        b=f1.read()
      else:
        await ctx.send("Guru file to dfalo. Firse try karo pura.")
        return
    a=re.compile("\d{18}")
    l1=a.findall(b)
    c=len(l1)
    await ctx.send("**Choose any one for futher operation:-\nFor new quiz enter `'1'`\nTo continue the old one enter `'2'`\nIf none then enter cancel.**")
    msg=await time(ctx,bot,300,"**No response recieved ,process has been reverted try again.**")
    d= msg.content
    if d=="1":
      f1=open("quiz.txt","w")
      i=0
      while i<c:
        f1.write(f"{l1[i]}|{1}"+"\n")
        i+=1
      await ctx.send("File has been created")
      return
    elif d=="2":
      f1=open("quiz.txt","r")
      a1=f1.readlines()
      a2=len(a1)
      dic={}
      for item in a1:
        l2=item.split("|")
        dic[l2[0]]=int(l2[1])
      await ctx.send("**Choose any one for futher operation:-\nFor final result enter `'1'`\nTo continue enterting scores enter `'2'`\nIf none then enter cancel.**")
      msg=await time(ctx,bot,300,"**No response recieved ,process has been reverted try again.**")
      a1=msg.content
      if a1=="1":
        l3=[]
        st=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        await ctx.send("**Final Score**")
        o=0
        for i in st:
          if o<50:
            f=f"<@{i[0]}> - {i[1]}"
            l3.append(f)
            o+=1
          else:
            l4="\n".join(l3)
            await ctx.send(f"`{l4}`")
            l3=[]
            o=0
        if 0<o<50:
          l4="\n".join(l3)
          await ctx.send(f"`{l4}`")
      elif a1=="2":
        for i in l1:
          if i in dic.keys():
            dic[i]+=1
          else:
            dic[i]=1
        l3=[]
        st=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        for i in st:
          f=f"<@{i[0]}> - {i[1]}"
          l3.append(f)
          l4="\n".join(l3)
        f1.close()
        f1=open("quiz.txt","w")
        o=0
        l3=[]
        await ctx.send(f"Final Score")
        for i in st:
          f1.write(f"{i[0]}|{i[1]}"+"\n")
          if o<50:
            f=f"<@{i[0]}> - {i[1]}"
            l3.append(f)
            o+=1
          else:
            l4="\n".join(l3)
            await ctx.send(f"`{l4}`")
            l3=[]
            o=0
        if 0<o<50:
          l4="\n".join(l3)
          await ctx.send(f"`{l4}`")
        await ctx.send("Scores has been updated")
      elif a1.lower()=="cancel":
        await ctx.send("wokay")
        return
      else:
        await ctx.send("Wrong selection , try again from start")
    elif d.lower()=="cancel":
      await ctx.send("wokay")
      return
    else:
      await ctx.send("Wrong selection , try again from start")
    





@bot.command()
async def slot(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("2mins will be given for each entry.\nEnter group no.:")
    a = True
    while a == True:
        try:
            msg = await bot.wait_for("message", timeout=120, check=check)
        except asyncio.TimeoutError:
            await ctx.send("`Time's up. Process has been cancelled, try again`"
                           )
            return

        a1 = int(msg.content)
        a4 = str(msg.content)
        a2 = len(msg.content)
        if type(a1) == int:
            if 1 < a2 < 3:
                await ctx.send(
                    "Now Enter the team names.\nEnter 'Stop' when the group is to be filled with lesser members.\nEnter 'Cancel' to stop the process. \n(Per group limit is 20 only)"
                )
                a = False
            else:
                await ctx.send("Group no. should be 2 digits long")
                a = True
        else:
            await ctx.send("Group no, should be an integer number")
            a = True
    i = 0
    b = []
    while i < 20:
        await ctx.send("Team no {}".format(i + 1))
        try:
            msg = await bot.wait_for("message", timeout=120, check=check)
        except asyncio.Timeouterror:
            await ctx.send("`Time's up, process has been cancelled try again.`"
                           )
            return
        b1 = msg.content
        if b1.lower() == "cancel":
            await ctx.send("The process has been cancelled.")
            return
        elif b1.lower() == 'stop':
            i = 20
            await ctx.send("Stopped entering process.")
        else:
            b.append(b1)
            i += 1
    im=Image.open("vgg.png")
    mio = await ctx.send("**Started entering Team records**")
    font2 = ImageFont.truetype("fonts/Roboto-mono.ttf",40)
    font1 = ImageFont.truetype("fonts/Collegehm.ttf",0)
    font = ImageFont.truetype("fonts/Landm.otf",50)
    a = [30,600]
    ko=[400, 465, 530, 595, 660, 725, 790, 855, 920, 985,400, 465, 530, 595, 660, 725, 790, 855, 920, 985]
    col=(255,255,255)
    d = ImageDraw.Draw(im)
    mn=len(b)
    i=0
    while i<10:
        draw = d.text((a[0], ko[i]), f"{i+1}.{b[i]}", col, font=font2)
        await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(b[i]))
        i+=1
    while 9<i<mn:
        draw = d.text((a[1], ko[i]), f"{i+1}.{b[i]}", col, font=font2)
        await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(b[i]))
        i+=1
    im.save("res.png")
    await mio.edit(content="**Successfully entered all the records <a:emoji_55:856633188485955584>,uploading the file**")
    await ctx.send(file=discord.File("res.png"))
    l2 = "\n".join(b)
    await ctx.send("**__Group no. {}__\n{}**".format(a4, l2))


@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    a = ctx.guild.roles
    b = ["Result Manager", "Result creator"]
    z = []
    d = len(a)
    a1 = ctx.guild.channels
    a2 = discord.utils.get(a1, name="points-table-data")
    i = 0
    while i < d:
        if b[0] in str(a[i]):
            z.append("m")
            i += 1
        elif b[1] in str(a[i]):
            z.append("c")
            i += 1
        else:
            i += 1
    if str(a2) == "points-table-data":
        z.append("ch")
    a4 = discord.utils.get(a, name=b[0])
    a5 = discord.utils.get(a, name=b[1])
    if len(z) == 2 and str(a2) != "None":
        lo = await ctx.send("Chill dude. It has been already done.")
        await asyncio.sleep(5)
        await lo.delete
    if len(z) == 0:
        role1 = await ctx.guild.create_role(name=b[0],
                                            color=discord.Color(0x2943DC))
        role2 = await ctx.guild.create_role(name=b[1],
                                            color=discord.Color(0x0A80DC))
        a3 = await ctx.guild.create_text_channel("points table data")
        await a3.set_permissions(a5,
                                 read_messages=True,
                                 send_messages=False,
                                 view_channel=True)
        await a3.set_permissions(a4,
                                 read_messages=True,
                                 send_messages=True,
                                 view_channel=True)
        await a3.set_permissions(ctx.guild.default_role,
                                 read_messages=False,
                                 send_messages=False,
                                 view_channel=False)
        embed = discord.Embed(
            description="I will be creating 2 roles namely{} and {}\n".format(
                role1.mention, role2.mention),
            color=discord.Color(red))
        l = "{}\nThis role gives permission to use result creation command\n\n{}\nThis roles gives permission to manage and to delete saved result data\n\n{} channel has been created where the backup will be uploaded of each record.It's still under development so it might have some issues while running.Don't delete or rename this channel as it will affect the working of the bot.".format(
            role2.mention, role1.mention, a3.mention)
        embed.add_field(name="ROLE INFORMATION", value=l)
        await ctx.send(embed=embed)
    i = 0
    z = []
    while i < d:
        if b[0] in str(a[i]):
            z.append("m")
            i += 1
        elif b[1] in str(a[i]):
            z.append("c")
            i += 1
        else:
            i += 1
    if str(a2) == "points-table-data":
        z.append("ch")
    if "c" not in z:
        role2 = await ctx.guild.create_role(name=b[1],
                                            color=discord.Color(0x0A80DC))
        embed = discord.Embed(
            description=
            "Seems like {} role is missong so it has been created.\n\nThis role gives permission to use result creation command.\n Assign this role to the members and get started"
            .format(role2.mention),
            color=discord.Color(red))
        await ctx.send(embed=embed)
    if "m" not in z:
        role1 = await ctx.guild.create_role(name=b[0],
                                            color=discord.Color(0x2943DC))
        embed = discord.Embed(
            description=
            "Seems like {} role eas missong so it has been created.\n\nThis roles gives permission to manage and to delete saved result data\n Assign this role to the members and get started"
            .format(role1.mention),
            color=discord.Color(red))
        await ctx.send(embed=embed)
    if "ch" not in z:
        overwrites = {
            ctx.guild.default_role:
            discord.PermissionOverwrite(read_messages=False,
                                        send_messages=False,
                                        view_channel=False),
            a4:
            discord.PermissionOverwrite(read_messages=True,
                                        send_messages=True,
                                        view_channel=True),
            a5:
            discord.PermissionOverwrite(read_messages=True,
                                        send_messages=False,
                                        view_channel=True)
        }
        a3 = await ctx.guild.create_text_channel("points table data",
                                                 overwrites=overwrites)
        embed = discord.Embed(
            description=
            "{} channel has been created where the backup will be uploaded of each record.It's still under development so it might have some issues while running.Don't delete or rename this channel as it will affect the working of the bot."
            .format(a3.mention),
            color=discord.Color(red))
        await ctx.send(embed=embed)


@setup.error
async def setup_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            description="You must have admin perms to use this command",
            color=discord.Color(red))
        await ctx.send(embed=embed)

async def fcreate(ctx):
  a1=os.listdir()
  n1=str(ctx.author.id)
  if n1 in a1:
    return
  else:
    a2= str(f"{ctx.author.id}")
    os.makedirs(a2)
    a3=str(f"{ctx.author.id}/rec.txt")
    f1=open(a3,"w")
    f1.close()
    a1=True
    return a1
@bot.command()
async def new(ctx):
  await vgret(ctx)

@bot.command()
@commands.has_any_role("Result creator", "Result Manager")
async def rest(ctx,*,a):
  a1=await fcreate(ctx)
  if a1==True:
    await cembed(ctx,red,"Your private folders have been created,you can use the saved data in all the servers where the bot exists",None)
  await res(ctx,bot,a)

@rest.error
async def res_error(ctx, error):
    red = int("ff0000", 16)
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        file = discord.File('asta.gif', filename="image.gif")
        embed = discord.Embed(
            title="ERROR!",
            description=
            "`{}rest [slotlist]`\n Run the command in the following format".
            format(prefix),
            color=discord.Color(red))
        embed.set_image(url="attachment://image.gif")
        await ctx.send(embed=embed, file=file)
    if isinstance(error, commands.MissingAnyRole):
        embed = discord.Embed(
            description=
            "You must have one of the following roles to use this command:-\n\n1) Result Manager\n2) Result creator",
            color=discord.Color(red))
        await ctx.send(embed=embed)
@bot.command()
@commands.has_any_role("Result creator", "Result Manager")
async def rt(ctx):
  a1=await fcreate(ctx)
  if a1==True:
    await cembed(ctx,red,"Your private folders have been created,you can use the saved data in all the servers where the bot exists",None)
  await restt(ctx,bot)

@rt.error
async def rt_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        embed = discord.Embed(
            description=
            "You must have one of the following roles to use this command:-\n\n1) Result Manager\n2) Result creator",
            color=discord.Color(red))
        await ctx.send(embed=embed)
@bot.command()
@commands.has_any_role("Result creator", "Result Manager")
async def res23(ctx, *, a):
    a1 = ctx.guild.channels
    red = int("ff0000", 16)
    a2 = discord.utils.get(a1, name="points-table-data")
    if str(a2) == "None":
        embed = discord.Embed(
            description=
            "Unable to fetch the backup channel created by the bot. use `{}setup` command to remove this issue."
            .format(prefix),
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    p = re.compile('Team.*')
    rawlist = p.findall(a)
    testvalue = len(rawlist)
    await ctx.message.delete()
    idlist = []
    teamlist = []
    killpoint1 = []
    killpoint2 = []
    matchplay = []
    pospoint1 = []
    pospoint2 = []
    chicken = []
    i = 0
    while i < testvalue:
        chicken.append(0)
        i += 1

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    ton = open("weekdata(2-3)/rec.txt", "a+")
    kl = open("weekdata(2-3)/Days(2-3).txt", "r+")
    days = int(kl.read(1))
    if days == 6:
        embed = discord.Embed(
            title="Weekly data collected",
            description=
            " Data of past 7 matches has already been collected, further match data cannot be sotred until weekly results have been created. Use the command ` {}weekly` to get the weekly result"
            .format(prefix),
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    else:
        poi = datetime.datetime.now()
        i = "weekdata(2-3)/Day{}.txt".format(days + 1)
        tor = open(i, "w")
    for item in rawlist:
        rie = item.replace("Team", "")
        teamlist.append(rie)
    if len(teamlist) < 3:
        await ctx.send(
            "Improper data entered, process has been cancelled try again")
        return
    i = 0
    a = """**Now enter the details of the teams being asked in the Following format.**
  
  **__Format__:-**
  `[Matches played],[Rank in match 1,enter 0 if not played],[Kills in match 1,enter 0 if no kills or not played],[Rank in match 2 , enter 0 if not played],[Kills in match enter 0 if no kills or match not played]`
  
  5 minutes will be given for each entry.
  
  **Enter cancel to quit the process at any stage.**"""
    embed = discord.Embed(title="DAY {} match data entry".format(days + 1),
                          description=a,
                          color=discord.Color(red))
    embed.set_footer(text="MONKEY D. LUFFY")
    await ctx.send(embed=embed)
    while i < testvalue:
        q = await ctx.send("""**Slot no.{} team {}**""".format(
            i + 1, teamlist[i]))
        try:
            msg = await bot.wait_for('message', timeout=300, check=check)
        except asyncio.TimeoutError:
            await ctx.send(
                'You didn\'t answer in time, please be quicker next time!')
            return
        g = msg.content
        h = g.split(",")
        if len(h) == 5:
            matchplay.append(int(h[0]))
            if int(h[1]) == 1:
                chicken[i] = chicken[i] + 1
                await ctx.send("1 up")
            pospoint1.append(int(h[1]))
            if int(h[3]) == 1:
                chicken[i] = chicken[i] + 1
                await ctx.send("2 up")
            pospoint2.append(int(h[3]))
            killpoint1.append(int(h[2]))
            killpoint2.append(int(h[4]))
            i += 1
        elif g.lower() == "cancel":
            await ctx.send("`Result creation has been cancelled`")
            return
        else:
            embed1 = discord.Embed(
                description=
                "**Values entered in inappropriate manner,try again from start**",
                color=discord.Color(red))
            await ctx.send(embed=embed1)
    totalpoint = []
    killf = []
    posf = []
    i = 0
    pos = [
        0, 15, 12, 10, 8, 6, 4, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0
    ]
    while i < testvalue:
        e = killpoint1[i] + killpoint2[i]
        killf.append(e)
        c = pos[pospoint1[i]] + pos[pospoint2[i]]
        posf.append(c)
        i += 1
    i = 0
    while i < testvalue:
        a = killf[i] + posf[i]
        totalpoint.append(a)
        i += 1

    async def sheet():
        workbook = xlsxwriter.Workbook('Pointstable.xlsx')
        worksheet = workbook.add_worksheet()
        titles = [
            "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
            "Total pts"
        ]
        i = 1
        place = []
        while i < (testvalue + 1):
            place.append(i)
            i += 1
            worksheet.write_row(0, 0, titles)
            worksheet.write_column(1, 0, place)
            worksheet.write_column(1, 1, ntl)
            worksheet.write_column(1, 2, nm)
            worksheet.write_column(1, 3, nc)
            worksheet.write_column(1, 4, np)
            worksheet.write_column(1, 5, nk)
            worksheet.write_column(1, 6, nt)
        workbook.close()
        await ctx.send(file=discord.File("Pointstable.xlsx"))

    x = PrettyTable()
    x.field_names = [
        "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
        "Total pts"
    ]
    i = 0
    e = 0
    clone = totalpoint.copy()
    clone.sort(reverse=True)
    elist = []
    ntl = []
    nm = []
    np = []
    nk = []
    nt = []
    nc = []
    while i < testvalue:
        if e in elist:
            e += 1
        else:
            if totalpoint[e] == clone[i]:
                ntl.append(str(teamlist[e]))
                nm.append(str(matchplay[e]))
                np.append(str(posf[e]))
                nk.append(str(killf[e]))
                nt.append(str(totalpoint[e]))
                nc.append(str(chicken[e]))
                i += 1
                elist.append(e)
                e = 0
            else:
                e += 1
    q = True
    ji = len(ntl)
    i = 0
    while q == True:
        if i == ji - 1:
            q = False
        elif clone[i] == clone[i + 1]:
            if nk[i] < nk[i + 1]:
                c1, c2, c3, c4, c5, c6 = ntl[i], nm[i], nc[i], np[i], nk[
                    i], nt[i]
                c11, c12, c13, c14, c15, c16 = ntl[i + 1], nm[i + 1], nc[
                    i + 1], np[i + 1], nk[i + 1], nt[i + 1]
                ntl[i], nm[i], nc[i], np[i], nk[i], nt[
                    i] = c11, c12, c13, c14, c15, c16
                ntl[i + 1], nm[i + 1], nc[i + 1], np[i + 1], nk[i + 1], nt[
                    i + 1] = c1, c2, c3, c4, c5, c6
                i = 0
            else:
                i += 1
        else:
            i += 1
    e = 0
    while e < ji:
        x.add_row([(i + 1), ntl[e], nm[e], nc[e], np[e], nk[e], nt[e]])
        e += 1
    embed = discord.Embed(title="Points table",
                          description=x,
                          color=discord.Color(red))
    await ctx.send(embed=embed)
    q = True
    while q:
        await ctx.send(
            "**Choose from the options given below\nTo make chnages to the points of a specific Team type `'1'`\nTo enter record of a new team type `'2'`\nTo save and make the result type `'3'`**"
        )
        try:
            msg = await bot.wait_for("message", timeout=300, check=check)
        except:
            await ctx.send(
                "You didn't answered so the process has been cancelled")
            return
        o = msg.content
        x = """**From the previous points table preview enter the changed data with the unchanged data as entered before in the given format.
      
      **__Format__:-**[Place of team according to the ponints table preview],[Matches played],[Rank in match 1,enter 0 if not played],[Kills in match 1,enter 0 if no kills or not played],[Rank in match 2 , enter 0 if not played],[Kills in match enter 0 if no kills or match not played]**"""
        c = discord.Embed(title="CORRECTION FORMAT",
                          description=x,
                          color=discord.Color(red))
        embed.set_footer(
            text=
            "if not answered in 5 mins the process will automatically be cancelled"
        )
        if o == "1":
            await ctx.send(embed=c)
            try:
                msg = await bot.wait_for("message", timeout=300, check=check)
            except asyncio.TimeoutError:
                await ctx.send(
                    "Didn't got any response, process has been reverted")
                return
            e = msg.content
            lis = e.split(",")
            h = []
            for item in lis:
                h.append(int(item))
            i = 0
            c = 0
            b = int(lis[0]) - 1
            if len(lis) == 6:
                io = True
                while io:
                    if ntl[b] == teamlist[c]:
                        matchplay[c] = h[1]
                        chicken[c] = 0
                        if h[2] == 1:
                            chicken[c] = chicken[c] + 1
                        if h[4] == 1:
                            chicken[c] = chicken[c] + 1
                        posf[c] = pos[h[2]] + pos[h[4]]
                        killf[c] = h[3] + h[5]
                        totalpoint[c] = posf[c] + killf[c]
                        c = 0
                        x = PrettyTable()
                        x.field_names = [
                            "Place", "Team name", "M", "Chicken", "Pos pts",
                            "Kill pts", "Total pts"
                        ]
                        i = 0
                        e = 0
                        clone = totalpoint.copy()
                        clone.sort(reverse=True)
                        elist = []
                        ntl = []
                        nm = []
                        np = []
                        nk = []
                        nt = []
                        nc = []
                        while i < testvalue:
                            if e in elist:
                                e += 1
                            else:
                                if totalpoint[e] == clone[i]:
                                    ntl.append(str(teamlist[e]))
                                    nm.append(str(matchplay[e]))
                                    np.append(str(posf[e]))
                                    nk.append(str(killf[e]))
                                    nt.append(str(totalpoint[e]))
                                    nc.append(str(chicken[e]))
                                    i += 1
                                    elist.append(e)
                                    e = 0
                                else:
                                    e += 1
                        q1 = True
                        await ctx.send("Details fetched")
                        ji = len(ntl)
                        i = 0
                        while q1 == True:
                            if i == ji - 1:
                                q1 = False
                            elif clone[i] == clone[i + 1]:
                                if nk[i] < nk[i + 1]:
                                    c1, c2, c3, c4, c5, c6 = ntl[i], nm[i], nc[
                                        i], np[i], nk[i], nt[i]
                                    c11, c12, c13, c14, c15, c16 = ntl[
                                        i +
                                        1], nm[i +
                                               1], nc[i +
                                                      1], np[i +
                                                             1], nk[i +
                                                                    1], nt[i +
                                                                           1]
                                    ntl[i], nm[i], nc[i], np[i], nk[i], nt[
                                        i] = c11, c12, c13, c14, c15, c16
                                    ntl[i + 1], nm[i + 1], nc[i + 1], np[
                                        i + 1], nk[i + 1], nt[
                                            i + 1] = c1, c2, c3, c4, c5, c6
                                    i = 0
                                else:
                                    i += 1
                            else:
                                i += 1
                        i = 0
                        while i < ji:
                            x.add_row([(i + 1), ntl[i], nm[i], nc[i], np[i],
                                       nk[i], nt[i]])
                            i += 1
                        embed = discord.Embed(title="Changed data",
                                              description=x,
                                              color=discord.Color(red))
                        await ctx.send(embed=embed)
                        io = False
                    else:
                        c += 1
            else:
                embed = discord.Embed(
                    description=
                    "**Values entered in inappropriate manner,try again**",
                    color=discord.Color(red))
                await ctx.send(embed=embed)
        elif o == "2":
            testvalue += 1
            ex = [
                "Enter the team name:", "Enter no. of matches played",
                "Enter rank in match 1,type 0 if not played:",
                "Enter no. of kills in match 1:",
                "Enter rank in match 2,enter 0 if not played",
                "Enter no. of kills in match 2"
            ]
            i = 0
            lis = []
            while i < 6:
                await ctx.send("**{}**".format(ex[i]))
                try:
                    msg = await bot.wait_for("message",
                                             timeout=300,
                                             check=check)
                except asyncio.TimeoutError:
                    await ctx.send(
                        "Didn't got any response, process has been reverted")
                    return
                lis.append(msg.content)
                i += 1
            teamlist.append(str(lis[0]))
            ch = 0
            del lis[0]
            matchplay.append(int(lis[0]))
            if lis[1] == 1:
                ch += 1
            if lis[3] == 1:
                ch += 1
            chicken.append(ch)
            posf.append(pos[int(lis[1])] + pos[int(lis[3])])
            killf.append(int(lis[2]) + int(lis[4]))
            totalpoint.append(pos[int(lis[1])] + pos[int(lis[3])] +
                              int(lis[2]) + int(lis[4]))
            x = PrettyTable()
            x.field_names = [
                "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
                "Total pts"
            ]
            i = 0
            e = 0
            clone = totalpoint.copy()
            clone.sort(reverse=True)
            elist = []
            ntl = []
            nm = []
            np = []
            nk = []
            nt = []
            nc = []
            while i < testvalue:
                if e in elist:
                    e += 1
                else:
                    if totalpoint[e] == clone[i]:
                        ntl.append(str(teamlist[e]))
                        nm.append(str(matchplay[e]))
                        np.append(str(posf[e]))
                        nk.append(str(killf[e]))
                        nt.append(str(totalpoint[e]))
                        nc.append(str(chicken[e]))
                        i += 1
                        elist.append(e)
                        e = 0
                    else:
                        e += 1
            q1 = True
            ji = len(ntl)
            i = 0
            while q1 == True:
                if i == ji - 1:
                    q1 = False
                elif clone[i] == clone[i + 1]:
                    if nk[i] < nk[i + 1]:
                        c1, c2, c3, c4, c5, c6 = ntl[i], nm[i], nc[i], np[
                            i], nk[i], nt[i]
                        c11, c12, c13, c14, c15, c16 = ntl[i + 1], nm[
                            i + 1], nc[i + 1], np[i + 1], nk[i + 1], nt[i + 1]
                        ntl[i], nm[i], nc[i], np[i], nk[i], nt[
                            i] = c11, c12, c13, c14, c15, c16
                        ntl[i + 1], nm[i + 1], nc[i + 1], np[i + 1], nk[
                            i + 1], nt[i + 1] = c1, c2, c3, c4, c5, c6
                        i = 0
                    else:
                        i += 1
                else:
                    i += 1
            i = 0
            while i < ji:
                x.add_row([(i + 1), ntl[i], nm[i], nc[i], np[i], nk[i], nt[i]])
                i += 1
            embed = discord.Embed(title="Points table",
                                  description=x,
                                  color=discord.Color(red))
            await ctx.send(embed=embed)
        elif o == "3":
            await sheet()
            i = 0
            place = []
            while i < testvalue:
                a = 1 + i
                place.append(str(a))
                i += 1
            im1 = Image.open('img1.png')
            im2 = Image.open('img2.png')

            async def get_concat_v_cut(im1, im2):
                i = 0
                mio = await ctx.send("**Started entering Team records**")
                dst = Image.new('RGB', (im2.width,
                                        (im1.height + testvalue * im2.height)))
                dst.paste(im1, (0, 0))
                font1 = ImageFont.truetype("fonts/Lemonb.otf", 200)
                font = ImageFont.truetype("fonts/Landm.otf", 300)
                a = [240, 500, 2500, 2900, 3500, 4030, 4550]
                im2.close()
                ko = 100
                mn = testvalue
                while i < mn:
                    im2 = Image.open('img2.png')
                    d = ImageDraw.Draw(im2)
                    draw = d.text((a[0], ko), place[i], (0, 0, 0), font=font1)
                    draw = d.text((a[1], ko), ntl[i], (0, 0, 0), font=font)
                    draw = d.text((a[2], ko), nc[i], (0, 0, 0), font=font1)
                    draw = d.text((a[3], ko), nm[i], (0, 0, 0), font=font1)
                    draw = d.text((a[4], ko), nk[i], (0, 0, 0), font=font1)
                    draw = d.text((a[5], ko), np[i], (0, 0, 0), font=font1)
                    draw = d.text((a[6], ko), nt[i], (0, 0, 0), font=font1)
                    dst.paste(im2, (0, (im1.height + i * im2.height)))
                    await mio.edit(
                        content=
                        "**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **"
                        .format(ntl[i]))
                    i += 1
                    im2.close()
                await mio.edit(
                    content=
                    "**Successfully entered all the records <a:emoji_55:856633188485955584>,uploading the file**"
                )
                dst.save("res.jpg")
                await ctx.send(file=discord.File("res.jpg"))

            await get_concat_v_cut(im1, im2)
            nl = "\n"
            wtl = ",".join(ntl)
            tor.writelines(wtl + nl)
            wm = ",".join(nm)
            tor.writelines(wm + nl)
            wc = ",".join(nc)
            tor.writelines(wc + nl)
            wp = ",".join(np)
            tor.writelines(wp + nl)
            wk = ",".join(nk)
            tor.writelines(wk + nl)
            wt = ",".join(nt)
            tor.writelines(wt + nl)
            tor.close()
            kl.seek(0)
            days += 1
            j1 = "**2-3pm result**\nDay{}.txt\n{}\nMade by:- {}".format(
                days, poi.strftime("%c"), ctx.author.mention)
            j2 = "Day{}.txt\n{}\n".format(days, poi.strftime("%c"))
            ton.write(j2)
            ton.seek(0)
            lm = "Day{}.txt".format(days)
            cv = ton.read()
            a4 = "weekdata(2-3)/" + lm
            await a2.send(j1, file=discord.File(a4))
            kl.write(str(days))
            ton.close()
            kl.close()
            q = False
        elif o.lower() == "cancel":
            await ctx.send("`Result creation has been cancelled`")
            return
        else:
            l = await ctx.send("**Inappropriate answer.**")
            await asyncio.sleep(5)
            await l.delete()


@res23.error
async def res23_error(ctx, error):
    red = int("ff0000", 16)
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        file = discord.File('asta.gif', filename="image.gif")
        embed = discord.Embed(
            title="ERROR!",
            description=
            "`{}res23 [slotlist]`\n Run the command in the following format".
            format(prefix),
            color=discord.Color(red))
        embed.set_image(url="attachment://image.gif")
        await ctx.send(embed=embed, file=file)
    if isinstance(error, commands.MissingAnyRole):
        embed = discord.Embed(
            description=
            "You must have one of the following roles to use this command:-\n\n1) Result Manager\n2) Result creator",
            color=discord.Color(red))
        await ctx.send(embed=embed)


@bot.command()
async def weekly23(ctx):
    f1 = open("weekdata(2-3)/rec.txt", "r")
    l1 = []
    z = 0
    k = 0
    p = 34
    a = f1.readline()
    f1.seek(0)
    if str(a) == "":
        embed = discord.Embed(
            title="NO FILE FOUND",
            description=
            "No files present in the directory, create point tables or upload data record files in order to make the Weekly result",
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    i = 0
    embed = discord.Embed(
        title="DATA RECORD",
        description=
        "Select Days whose data is to be processed further in the following format.\n n,n,n,....\n`{n represents the no. of day}`",
        color=discord.Color(red))
    while z == 0:
        a = f1.readline()
        f1.seek(0)
        ko = p * i
        f1.seek(ko)
        ko = len(list(a))
        if str(a) != "":
            k = 0
            while k < 3:
                if k == 0:
                    a = f1.readline()
                    k += 1
                elif k == 1:
                    b = f1.readline()
                    p = ko + len(list(b))
                    k += 1
                elif k == 2:
                    embed.add_field(name=a, value=b)
                    i += 1
                    break
        elif str(a) == "":
            z = 1

    await ctx.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", timeout=180, check=check)
    except asyncio.TimeoutError:
        await ctx.send(
            '**You took too long to reply. Process has been cancelled ,try again**'
        )
        return
    if str(msg.content.lower()) == "cancel":
        await ctx.send("`Result making process has been cancelled`")
        return
    a = (msg.content).split(",")
    t = len(a)
    b = "weekdata(2-3)/Day{}.txt".format(a[0])
    f2 = open(b, "r")
    wr = []
    i = 0
    while i < 20:
        wr.append(str(i + 1))
        i += 1
    wtl = []
    wm = []
    wc = []
    wp = []
    wk = []
    wt = []
    i = 0
    while i < 6:
        if i == 0:
            c = f2.readline()
        else:
            c = f2.readline()
        d = c.replace("\n", "")
        if i == 0:
            wtl = d.split(",")
            i += 1
        elif i == 1:
            f = d.split(",")
            wm = list(map(int, f))
            i += 1
        elif i == 2:
            f = d.split(",")
            wc = list(map(int, f))
            i += 1
        elif i == 3:
            f = d.split(",")
            wp = list(map(int, f))
            i += 1
        elif i == 4:
            f = d.split(",")
            wk = list(map(int, f))
            i += 1
        elif i == 5:
            f = d.split(",")
            wt = list(map(int, f))
            i += 1
    i = 1
    while i < t:
        aio = "weekdata(2-3)/Day{}.txt".format(a[i])
        f3 = open(aio, "r")
        ntl = []
        nm = []
        nc = []
        np = []
        nk = []
        nt = []
        e = 0
        while e < 6:
            if e == 0:
                c = f3.readline()
            else:
                c = f3.readline()
            d = c.replace("\n", "")
            if e == 0:
                ntl = d.split(",")
                e += 1
            elif e == 1:
                f = d.split(",")
                nm = list(map(int, f))
                e += 1
            elif e == 2:
                f = d.split(",")
                nc = list(map(int, f))
                e += 1
            elif e == 3:
                f = d.split(",")
                np = list(map(int, f))
                e += 1
            elif e == 4:
                f = d.split(",")
                nk = list(map(int, f))
                e += 1
            elif e == 5:
                f = d.split(",")
                nt = list(map(int, f))
                e += 1
        c = len(ntl)
        wtll = []
        for item in wtl:
            a1 = item.lower()
            a2 = a1.replace(" ", "")
            wtll.append(a2)
        ntll = []
        for item in ntl:
            a1 = item.lower()
            a2 = a1.replace(" ", "")
            ntll.append(a2)
        e = 0
        while e < c:
            if ntll[e] in wtll:
                d = wtll.index(ntll[e])
                wm[d] = wm[d] + nm[e]
                wc[d] = wc[d] + nc[e]
                wp[d] = wp[d] + np[e]
                wk[d] = wk[d] + nk[e]
                wt[d] = wt[d] + nt[e]
                e += 1
            else:
                wtl.append(ntl[e])
                wm.append(nm[e])
                wc.append(nc[e])
                wp.append(np[e])
                wk.append(nk[e])
                wt.append(nt[e])
                e += 1
        print("io")
        i += 1
    i = 0
    e = 0
    clone = wt.copy()
    clone.sort(reverse=True)
    elist = []
    ftl = []
    fm = []
    fp = []
    fk = []
    ft = []
    fc = []
    lo = len(wtl)
    while i < lo:
        if e in elist:
            e += 1
        else:
            if wt[e] == clone[i]:
                ftl.append(str(wtl[e]))
                fm.append(str(wm[e]))
                fc.append(str(wc[e]))
                fp.append(str(wp[e]))
                fk.append(str(wk[e]))
                ft.append(str(wt[e]))
                i += 1
                elist.append(e)
                e = 0
            else:
                e += 1
    im1 = Image.open('img1.png')
    im2 = Image.open('img2.png')

    async def get_concat_v_cut(im1, im2):
        i = 0
        mio = await ctx.send("**Started entering Team records**")
        dst = Image.new('RGB', (im2.width, (im1.height + 20 * im2.height)))
        dst.paste(im1, (0, 0))
        font1 = ImageFont.truetype("fonts/Lemonb.otf", 200)
        font = ImageFont.truetype("fonts/Landm.otf", 300)
        a = [240, 500, 2500, 2900, 3500, 4030, 4550]
        im2.close()
        ko = 100
        mn = 20
        while i < mn:
            im2 = Image.open('img2.png')
            d = ImageDraw.Draw(im2)
            draw = d.text((a[0], ko), wr[i], (0, 0, 0), font=font1)
            draw = d.text((a[1], ko), ftl[i], (0, 0, 0), font=font)
            draw = d.text((a[2], ko), fc[i], (0, 0, 0), font=font1)
            draw = d.text((a[3], ko), fm[i], (0, 0, 0), font=font1)
            draw = d.text((a[4], ko), fk[i], (0, 0, 0), font=font1)
            draw = d.text((a[5], ko), fp[i], (0, 0, 0), font=font1)
            draw = d.text((a[6], ko), ft[i], (0, 0, 0), font=font1)
            dst.paste(im2, (0, (im1.height + i * im2.height)))
            im2.close()
            i += 1
        dst.save("res.jpg")

    await get_concat_v_cut(im1, im2)
    await ctx.send(file=discord.File("res.jpg"))

    async def sheet():
        workbook = xlsxwriter.Workbook('Weekly-Pointstable.xlsx')
        worksheet = workbook.add_worksheet()
        titles = [
            "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
            "Total pts"
        ]
        i = 1
        place = []
        while i < (lo + 1):
            place.append(i)
            i += 1
            worksheet.write_row(0, 0, titles)
            worksheet.write_column(1, 0, wr)
            worksheet.write_column(1, 1, ftl)
            worksheet.write_column(1, 2, fm)
            worksheet.write_column(1, 3, fc)
            worksheet.write_column(1, 4, fp)
            worksheet.write_column(1, 5, fk)
            worksheet.write_column(1, 6, ft)
        workbook.close()
        await ctx.send(file=discord.File("Weekly-Pointstable.xlsx"))

    await sheet()
    f1.seek(0)
    f1.truncate()
    f1.close()
    embed = discord.Embed(
        title="DATA UTILISED",
        description=
        "Thus weeks points table data has been utilised.Therefore, selected files will be deleted. Backup of the data has been uploaded in form of csv file kindly use it in any kind need in future.",
        color=discord.Color(red))
    await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role("Result creator", "Result Manager")
async def res45(ctx, *, a):
    a1 = ctx.guild.channels
    red = int("ff0000", 16)
    a2 = discord.utils.get(a1, name="points-table-data")
    if str(a2) == "None":
        embed = discord.Embed(
            description=
            "Unable to fetch the backup channel created by the bot. use `{}setup` command to remove this issue."
            .format(prefix),
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    p = re.compile('Team.*')
    rawlist = p.findall(a)
    testvalue = len(rawlist)
    await ctx.message.delete()
    idlist = []
    teamlist = []
    killpoint1 = []
    killpoint2 = []
    matchplay = []
    pospoint1 = []
    pospoint2 = []
    chicken = []
    i = 0
    while i < testvalue:
        chicken.append(0)
        i += 1

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    ton = open("weekdata(4-5)/rec.txt", "a+")
    kl = open("weekdata(4-5)/Days(4-5).txt", "r+")
    days = int(kl.read(1))
    if days == 6:
        embed = discord.Embed(
            title="Weekly data collected",
            description=
            " Data of past 7 matches has already been collected, further match data cannot be sotred until weekly results have been created. Use the command ` {}weekly` to get the weekly result"
            .format(prefix),
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    else:
        poi = datetime.datetime.now()
        i = "weekdata(4-5)/Day{}.txt".format(days + 1)
        tor = open(i, "w")
    for item in rawlist:
        rie = item.replace("Team", "")
        teamlist.append(rie)
    if len(teamlist) < 3:
        await ctx.send(
            "Improper data entered, process has been cancelled try again")
        return
    i = 0
    a = """**Now enter the details of the teams being asked in the Following format.**
  
  **__Format__:-**
  `[Matches played],[Rank in match 1,enter 0 if not played],[Kills in match 1,enter 0 if no kills or not played],[Rank in match 2 , enter 0 if not played],[Kills in match enter 0 if no kills or match not played]`
  
  5 minutes will be given for each entry.
  
  **Enter cancel to quit the process at any stage.**"""
    embed = discord.Embed(title="DAY {} match data entry".format(days + 1),
                          description=a,
                          color=discord.Color(red))
    embed.set_footer(text="MONKEY D. LUFFY")
    await ctx.send(embed=embed)
    while i < testvalue:
        q = await ctx.send("""**Slot no.{} team {}**""".format(
            i + 1, teamlist[i]))
        try:
            msg = await bot.wait_for('message', timeout=600, check=check)
        except asyncio.TimeoutError:
            await ctx.send(
                'You didn\'t answer in time, please be quicker next time!')
            return
        g = msg.content
        h = g.split(",")
        if len(h) == 5:
            matchplay.append(int(h[0]))
            if int(h[1]) == 1:
                chicken[i] = chicken[i] + 1
                await ctx.send("1 up")
            pospoint1.append(int(h[1]))
            if int(h[3]) == 1:
                chicken[i] = chicken[i] + 1
                await ctx.send("2 up")
            pospoint2.append(int(h[3]))
            killpoint1.append(int(h[2]))
            killpoint2.append(int(h[4]))
            i += 1
        elif g.lower() == "cancel":
            await ctx.send("`Result creation has been cancelled`")
            return
        else:
            embed1 = discord.Embed(
                description=
                "**Values entered in inappropriate manner,try again from start**",
                color=discord.Color(red))
            await ctx.send(embed=embed1)
    totalpoint = []
    killf = []
    posf = []
    i = 0
    pos = [
        0, 15, 12, 10, 8, 6, 4, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0
    ]
    while i < testvalue:
        e = killpoint1[i] + killpoint2[i]
        killf.append(e)
        c = pos[pospoint1[i]] + pos[pospoint2[i]]
        posf.append(c)
        i += 1
    i = 0
    while i < testvalue:
        a = killf[i] + posf[i]
        totalpoint.append(a)
        i += 1

    async def sheet():
        workbook = xlsxwriter.Workbook('Pointstable.xlsx')
        worksheet = workbook.add_worksheet()
        titles = [
            "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
            "Total pts"
        ]
        i = 1
        place = []
        while i < (testvalue + 1):
            place.append(i)
            i += 1
            worksheet.write_row(0, 0, titles)
            worksheet.write_column(1, 0, place)
            worksheet.write_column(1, 1, ntl)
            worksheet.write_column(1, 2, nm)
            worksheet.write_column(1, 3, nc)
            worksheet.write_column(1, 4, np)
            worksheet.write_column(1, 5, nk)
            worksheet.write_column(1, 6, nt)
        workbook.close()
        await ctx.send(file=discord.File("Pointstable.xlsx"))

    x = PrettyTable()
    x.field_names = [
        "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
        "Total pts"
    ]
    i = 0
    e = 0
    clone = totalpoint.copy()
    clone.sort(reverse=True)
    elist = []
    ntl = []
    nm = []
    np = []
    nk = []
    nt = []
    nc = []
    while i < testvalue:
        if e in elist:
            e += 1
        else:
            if totalpoint[e] == clone[i]:
                ntl.append(str(teamlist[e]))
                nm.append(str(matchplay[e]))
                np.append(str(posf[e]))
                nk.append(str(killf[e]))
                nt.append(str(totalpoint[e]))
                nc.append(str(chicken[e]))
                i += 1
                elist.append(e)
                e = 0
            else:
                e += 1
    ntl, nm, nc, np, nk, nt, ji = await ksort(ntl, nm, nc, np, nk, nt, clone)
    e = 0
    while e < ji:
        x.add_row([(e + 1), ntl[e], nm[e], nc[e], np[e], nk[e], nt[e]])
        e += 1
    embed = discord.Embed(title="Points table",
                          description=x,
                          color=discord.Color(red))
    await ctx.send(embed=embed)
    q = True
    while q:
        await ctx.send(
            "**Choose from the options given below\nTo make chnages to the points of a specific Team type `'1'`\nTo enter record of a new team type `'2'`\nTo save and make the result type `'3'`**"
        )
        try:
            msg = await bot.wait_for("message", timeout=300, check=check)
        except:
            await ctx.send(
                "You didn't answered so the process has been cancelled")
            return
        o = msg.content
        x = """**From the previous points table preview enter the changed data with the unchanged data as entered before in the given format.
      
      **__Format__:-**[Place of team according to the ponints table preview],[Matches played],[Rank in match 1,enter 0 if not played],[Kills in match 1,enter 0 if no kills or not played],[Rank in match 2 , enter 0 if not played],[Kills in match enter 0 if no kills or match not played]**
      
      if not answered in 5 mins the process will automatically be cancelled"""
        c = discord.Embed(title="CORRECTION FORMAT",
                          description=x,
                          color=discord.Color(red))
        if o == "1":
            await ctx.send(embed=c)
            try:
                msg = await bot.wait_for("message", timeout=300, check=check)
            except asyncio.TimeoutError:
                await ctx.send(
                    "Didn't got any response, process has been reverted")
                return
            await ctx.send("Details fetched")
            e = msg.content
            lis = e.split(",")
            h = []
            for item in lis:
                h.append(int(item))
            i = 0
            c = 0
            b = int(lis[0]) - 1
            if len(lis) == 6:
                io = True
                while io:
                    if ntl[b] == teamlist[c]:
                        matchplay[c] = h[1]
                        chicken[c] = 0
                        if h[2] == 1:
                            chicken[c] = chicken[c] + 1
                        if h[4] == 1:
                            chicken[c] = chicken[c] + 1
                        posf[c] = pos[h[2]] + pos[h[4]]
                        killf[c] = h[3] + h[5]
                        totalpoint[c] = posf[c] + killf[c]
                        c = 0
                        x = PrettyTable()
                        x.field_names = [
                            "Place", "Team name", "M", "Chicken", "Pos pts",
                            "Kill pts", "Total pts"
                        ]
                        i = 0
                        e = 0
                        clone = totalpoint.copy()
                        clone.sort(reverse=True)
                        elist = []
                        ntl = []
                        nm = []
                        np = []
                        nk = []
                        nt = []
                        nc = []
                        while i < testvalue:
                            if e in elist:
                                e += 1
                            else:
                                if totalpoint[e] == clone[i]:
                                    ntl.append(str(teamlist[e]))
                                    nm.append(str(matchplay[e]))
                                    np.append(str(posf[e]))
                                    nk.append(str(killf[e]))
                                    nt.append(str(totalpoint[e]))
                                    nc.append(str(chicken[e]))
                                    i += 1
                                    elist.append(e)
                                    e = 0
                                else:
                                    e += 1
                        ntl, nm, nc, np, nk, nt, ji = await ksort(
                            ntl, nm, nc, np, nk, nt, clone)
                        i = 0
                        while i < ji:
                            x.add_row([(i + 1), ntl[i], nm[i], nc[i], np[i],
                                       nk[i], nt[i]])
                            i += 1
                        embed = discord.Embed(title="Changed data",
                                              description=x,
                                              color=discord.Color(red))
                        await ctx.send(embed=embed)
                        io = False
                    else:
                        c += 1
            else:
                await msg.delete()
                embed = discord.Embed(
                    description=
                    "**Values entered in inappropriate manner,try again**",
                    color=discord.Color(red))
                await ctx.send(embed=embed)
        elif o == "2":
            testvalue += 1
            ex = [
                "Enter the team name:", "Enter no. of matches played",
                "Enter rank in match 1,type 0 if not played:",
                "Enter no. of kills in match 1:",
                "Enter rank in match 2,enter 0 if not played",
                "Enter no. of kills in match 2"
            ]
            i = 0
            lis = []
            while i < 6:
                await ctx.send("**{}**".format(ex[i]))
                try:
                    msg = await bot.wait_for("message",
                                             timeout=300,
                                             check=check)
                except asyncio.TimeoutError:
                    await ctx.send(
                        "Didn't got any response, process has been reverted")
                    return
                lis.append(msg.content)
                i += 1
            teamlist.append(str(lis[0]))
            ch = 0
            del lis[0]
            matchplay.append(int(lis[0]))
            if lis[1] == 1:
                ch += 1
            if lis[3] == 1:
                ch += 1
            chicken.append(ch)
            posf.append(pos[int(lis[1])] + pos[int(lis[3])])
            killf.append(int(lis[2]) + int(lis[4]))
            totalpoint.append(pos[int(lis[1])] + pos[int(lis[3])] +
                              int(lis[2]) + int(lis[4]))
            x = PrettyTable()
            x.field_names = [
                "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
                "Total pts"
            ]
            i = 0
            e = 0
            clone = totalpoint.copy()
            clone.sort(reverse=True)
            elist = []
            ntl = []
            nm = []
            np = []
            nk = []
            nt = []
            nc = []
            while i < testvalue:
                if e in elist:
                    e += 1
                else:
                    if totalpoint[e] == clone[i]:
                        x.add_row([(i + 1), teamlist[e], matchplay[e],
                                   chicken[e], posf[e], killf[e],
                                   totalpoint[e]])
                        ntl.append(str(teamlist[e]))
                        nm.append(str(matchplay[e]))
                        np.append(str(posf[e]))
                        nk.append(str(killf[e]))
                        nt.append(str(totalpoint[e]))
                        nc.append(str(chicken[e]))
                        i += 1
                        elist.append(e)
                        e = 0
                    else:
                        e += 1
            ntl, nm, nc, np, nk, nt, ji = await ksort(ntl, nm, nc, np, nk, nt,
                                                      clone)
            i = 0
            while i < ji:
                x.add_row([(i + 1), ntl[i], nm[i], nc[i], np[i], nk[i], nt[i]])
                i += 1
            embed = discord.Embed(title="Points table",
                                  description=x,
                                  color=discord.Color(red))
            await ctx.send(embed=embed)
        elif o == "3":
            await sheet()
            i = 0
            place = []
            while i < testvalue:
                a = 1 + i
                place.append(str(a))
                i += 1
            im1 = Image.open('img1.png')
            im2 = Image.open('img2.png')

            async def get_concat_v_cut(im1, im2):
                i = 0
                mio = await ctx.send("**Started entering Team records**")
                dst = Image.new('RGB', (im2.width,
                                        (im1.height + testvalue * im2.height)))
                dst.paste(im1, (0, 0))
                font1 = ImageFont.truetype("fonts/Lemonb.otf", 200)
                font = ImageFont.truetype("fonts/Landm.otf", 300)
                a = [240, 500, 2500, 2900, 3500, 4030, 4550]
                im2.close()
                ko = 100
                mn = testvalue
                while i < mn:
                    im2 = Image.open('img2.png')
                    d = ImageDraw.Draw(im2)
                    draw = d.text((a[0], ko), place[i], (0, 0, 0), font=font1)
                    draw = d.text((a[1], ko), ntl[i], (0, 0, 0), font=font)
                    draw = d.text((a[2], ko), nc[i], (0, 0, 0), font=font1)
                    draw = d.text((a[3], ko), nm[i], (0, 0, 0), font=font1)
                    draw = d.text((a[4], ko), nk[i], (0, 0, 0), font=font1)
                    draw = d.text((a[5], ko), np[i], (0, 0, 0), font=font1)
                    draw = d.text((a[6], ko), nt[i], (0, 0, 0), font=font1)
                    dst.paste(im2, (0, (im1.height + i * im2.height)))
                    await mio.edit(
                        content=
                        "**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **"
                        .format(ntl[i]))
                    i += 1
                    im2.close()
                await mio.edit(
                    content=
                    "**Successfully entered all the records <a:emoji_55:856633188485955584>,uploading the file**"
                )
                dst.save("res.jpg")
                await ctx.send(file=discord.File("res.jpg"))

            await get_concat_v_cut(im1, im2)
            nl = "\n"
            wtl = ",".join(ntl)
            tor.writelines(wtl + nl)
            wm = ",".join(nm)
            tor.writelines(wm + nl)
            wc = ",".join(nc)
            tor.writelines(wc + nl)
            wp = ",".join(np)
            tor.writelines(wp + nl)
            wk = ",".join(nk)
            tor.writelines(wk + nl)
            wt = ",".join(nt)
            tor.writelines(wt + nl)
            tor.close()
            kl.seek(0)
            days += 1
            j1 = "**4-5pm result**\nDay{}.txt\n{}\nMade by:- {}".format(
                days, poi.strftime("%c"), ctx.author.mention)
            j2 = "Day{}.txt\n{}\n".format(days, poi.strftime("%c"))
            ton.write(j2)
            ton.seek(0)
            lm = "Day{}.txt".format(days)
            cv = ton.read()
            a4 = "weekdata(4-5)/" + lm
            await a2.send(j1, file=discord.File(a4))
            kl.write(str(days))
            ton.close()
            kl.close()
            q = False
        elif o.lower() == "cancel":
            await ctx.send("`Result creation has been cancelled`")
            return
        else:
            l = await ctx.send("**Inappropriate answer.**")
            await asyncio.sleep(5)
            await l.delete()


@res45.error
async def res45_error(ctx, error):
    red = int("ff0000", 16)
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        file = discord.File('asta.gif', filename="image.gif")
        embed = discord.Embed(
            title="ERROR!",
            description=
            "`{}res45 [slotlist]`\n Run the command in the following format".
            format(prefix),
            color=discord.Color(red))
        embed.set_image(url="attachment://image.gif")
        await ctx.send(embed=embed, file=file)
    if isinstance(error, commands.MissingAnyRole):
        embed = discord.Embed(
            description=
            "You must have one of the following roles to use this command:-\n\n1) Result Manager\n2) Result creator",
            color=discord.Color(red))
        await ctx.send(embed=embed)


@bot.command()
async def weekly45(ctx):
    f1 = open("weekdata(4-5)/rec.txt", "r")
    l1 = []
    z = 0
    k = 0
    p = 34
    a = f1.readline()
    f1.seek(0)
    if str(a) == "":
        embed = discord.Embed(
            title="NO FILE FOUND",
            description=
            "No files present in the directory, create point tables or upload data record files in order to make the Weekly result",
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    i = 0
    embed = discord.Embed(
        title="DATA RECORD",
        description=
        "Select Days whose data is to be processed further in the following format.\n n,n,n,....\n`{n represents the no. of day}`",
        color=discord.Color(red))
    while z == 0:
        a = f1.readline()
        f1.seek(0)
        ko = p * i
        f1.seek(ko)
        ko = len(list(a))
        if str(a) != "":
            k = 0
            while k < 3:
                if k == 0:
                    a = f1.readline()
                    k += 1
                elif k == 1:
                    b = f1.readline()
                    p = ko + len(list(b))
                    k += 1
                elif k == 2:
                    embed.add_field(name=a, value=b)
                    i += 1
                    break
        elif str(a) == "":
            z = 1

    await ctx.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", timeout=180, check=check)
    except asyncio.TimeoutError:
        await ctx.send(
            '**You took too long to reply. Process has been cancelled ,try again**'
        )
        return
    if str(msg.content.lower()) == "cancel":
        await ctx.send("`Result making process has been cancelled`")
        return
    a = (msg.content).split(",")
    t = len(a)
    b = "weekdata(4-5)/Day{}.txt".format(a[0])
    f2 = open(b, "r")
    wr = []
    i = 0
    while i < 20:
        wr.append(str(i + 1))
        i += 1
    wtl = []
    wm = []
    wc = []
    wp = []
    wk = []
    wt = []
    i = 0
    while i < 6:
        if i == 0:
            c = f2.readline()
        else:
            c = f2.readline()
        d = c.replace("\n", "")
        if i == 0:
            wtl = d.split(",")
            i += 1
        elif i == 1:
            f = d.split(",")
            wm = list(map(int, f))
            i += 1
        elif i == 2:
            f = d.split(",")
            wc = list(map(int, f))
            i += 1
        elif i == 3:
            f = d.split(",")
            wp = list(map(int, f))
            i += 1
        elif i == 4:
            f = d.split(",")
            wk = list(map(int, f))
            i += 1
        elif i == 5:
            f = d.split(",")
            wt = list(map(int, f))
            i += 1
    i = 1
    while i < t:
        aio = "weekdata(4-5)/Day{}.txt".format(a[i])
        f3 = open(aio, "r")
        ntl = []
        nm = []
        nc = []
        np = []
        nk = []
        nt = []
        e = 0
        while e < 6:
            if e == 0:
                c = f3.readline()
            else:
                c = f3.readline()
            d = c.replace("\n", "")
            if e == 0:
                ntl = d.split(",")
                e += 1
            elif e == 1:
                f = d.split(",")
                nm = list(map(int, f))
                e += 1
            elif e == 2:
                f = d.split(",")
                nc = list(map(int, f))
                e += 1
            elif e == 3:
                f = d.split(",")
                np = list(map(int, f))
                e += 1
            elif e == 4:
                f = d.split(",")
                nk = list(map(int, f))
                e += 1
            elif e == 5:
                f = d.split(",")
                nt = list(map(int, f))
                e += 1
        c = len(ntl)
        wtll = []
        for item in wtl:
            a1 = item.lower()
            a2 = a1.replace(" ", "")
            wtll.append(a2)
        ntll = []
        for item in ntl:
            a1 = item.lower()
            a2 = a1.replace(" ", "")
            ntll.append(a2)
        e = 0
        while e < c:
            if ntll[e] in wtll:
                d = wtll.index(ntll[e])
                wm[d] = wm[d] + nm[e]
                wc[d] = wc[d] + nc[e]
                wp[d] = wp[d] + np[e]
                wk[d] = wk[d] + nk[e]
                wt[d] = wt[d] + nt[e]
                e += 1
            else:
                wtl.append(ntl[e])
                wm.append(nm[e])
                wc.append(nc[e])
                wp.append(np[e])
                wk.append(nk[e])
                wt.append(nt[e])
                e += 1
        i += 1
    i = 0
    e = 0
    clone = wt.copy()
    clone.sort(reverse=True)
    elist = []
    ftl = []
    fm = []
    fp = []
    fk = []
    ft = []
    fc = []
    print(wt)
    print(wtl)
    lo = len(wt)
    while i < lo:
        if e in elist:
            e += 1
        else:
            if wt[e] == clone[i]:
                ftl.append(str(wtl[e]))
                fm.append(str(wm[e]))
                fc.append(str(wc[e]))
                fp.append(str(wp[e]))
                fk.append(str(wk[e]))
                ft.append(str(wt[e]))
                i += 1
                elist.append(e)
                e = 0
    
            else:
                e += 1
    im1 = Image.open('img1.png')
    im2 = Image.open('img2.png')

    async def get_concat_v_cut(im1, im2):
        i = 0
        mio = await ctx.send("**Started entering Team records**")
        dst = Image.new('RGB', (im2.width, (im1.height + 20 * im2.height)))
        dst.paste(im1, (0, 0))
        font1 = ImageFont.truetype("fonts/Lemonb.otf", 200)
        font = ImageFont.truetype("fonts/Landm.otf", 300)
        a = [240, 500, 2500, 2900, 3500, 4030, 4550]
        im2.close()
        ko = 100
        mn = 20
        while i < mn:
            im2 = Image.open('img2.png')
            d = ImageDraw.Draw(im2)
            draw = d.text((a[0], ko), wr[i], (0, 0, 0), font=font1)
            draw = d.text((a[1], ko), ftl[i], (0, 0, 0), font=font)
            draw = d.text((a[2], ko), fc[i], (0, 0, 0), font=font1)
            draw = d.text((a[3], ko), fm[i], (0, 0, 0), font=font1)
            draw = d.text((a[4], ko), fk[i], (0, 0, 0), font=font1)
            draw = d.text((a[5], ko), fp[i], (0, 0, 0), font=font1)
            draw = d.text((a[6], ko), ft[i], (0, 0, 0), font=font1)
            dst.paste(im2, (0, (im1.height + i * im2.height)))
            im2.close()
            i += 1
        dst.save("res.jpg")

    await get_concat_v_cut(im1, im2)
    await ctx.send(file=discord.File("res.jpg"))
    tor=open("restu.txt","w")
    nl = "\n"
    wtl = ",".join(ftl)
    tor.writelines(wtl + nl)
    wm = ",".join(fm)
    tor.writelines(wm + nl)
    wc = ",".join(fc)
    tor.writelines(wc + nl)
    wp = ",".join(fp)
    tor.writelines(wp + nl)
    wk = ",".join(fk)
    tor.writelines(wk + nl)
    wt = ",".join(ft)
    tor.writelines(wt + nl)
    tor.close()
    async def sheet():
        workbook = xlsxwriter.Workbook('Weekly-Pointstable.xlsx')
        worksheet = workbook.add_worksheet()
        titles = [
            "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
            "Total pts"
        ]
        i = 1
        place = []
        while i < (lo + 1):
            place.append(i)
            i += 1
            worksheet.write_row(0, 0, titles)
            worksheet.write_column(1, 0, wr)
            worksheet.write_column(1, 1, ftl)
            worksheet.write_column(1, 2, fm)
            worksheet.write_column(1, 3, fc)
            worksheet.write_column(1, 4, fp)
            worksheet.write_column(1, 5, fk)
            worksheet.write_column(1, 6, ft)
        workbook.close()
        await ctx.send(file=discord.File("Weekly-Pointstable.xlsx"))

    await sheet()
    f1.seek(0)
    f1.truncate()
    f1.close()
    embed = discord.Embed(
        title="DATA UTILISED",
        description=
        "Thus weeks points table data has been utilised.Therefore, selected files will be deleted. Backup of the data has been uploaded in form of csv file kindly use it in any kind need in future.",
        color=discord.Color(red))
    await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role("Result creator", "Result Manager")
async def t2(ctx, *, a):
    a1 = ctx.guild.channels
    red = int("ff0000", 16)
    a2 = discord.utils.get(a1, name="points-table-data")
    if str(a2) == "None":
        embed = discord.Embed(
            description=
            "Unable to fetch the backup channel created by the bot. use `{}setup` command to remove this issue."
            .format(prefix),
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    p = re.compile('Team.*')
    rawlist = p.findall(a)
    testvalue = len(rawlist)
    await ctx.message.delete()
    idlist = []
    teamlist = []
    killpoint1 = []
    killpoint2 = []
    matchplay = []
    pospoint1 = []
    pospoint2 = []
    chicken = []
    i = 0
    while i < testvalue:
        chicken.append(0)
        i += 1

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    ton = open("t2weekdata/rec.txt", "a+")
    kl = open("t2weekdata/Days.txt", "r+")
    days = int(kl.read(1))
    if days == 6:
        embed = discord.Embed(
            title="Weekly data collected",
            description=
            " Data of past 7 matches has already been collected, further match data cannot be sotred until weekly results have been created. Use the command ` {}weekly` to get the weekly result"
            .format(prefix),
            color=discord.Color(red))
        await ctx.send(embed=embed)
        return
    else:
        poi = datetime.datetime.now()
        i = "t2weekdata/Day{}.txt".format(days + 1)
        tor = open(i, "w")
    for item in rawlist:
        rie = item.replace("Team", "")
        teamlist.append(rie)
    if len(teamlist) < 3:
        await ctx.send(
            "Improper data entered, process has been cancelled try again")
        return
    i = 0
    a = """**Now enter the details of the teams being asked in the Following format.**
  
  **__Format__:-**
  `[Matches played],[Rank in match 1,enter 0 if not played],[Kills in match 1,enter 0 if no kills or not played],[Rank in match 2 , enter 0 if not played],[Kills in match enter 0 if no kills or match not played]`
  
  5 minutes will be given for each entry.
  
  **Enter cancel to quit the process at any stage.**"""
    embed = discord.Embed(title="DAY {} match data entry".format(days + 1),
                          description=a,
                          color=discord.Color(red))
    embed.set_footer(text="MONKEY D. LUFFY")
    await ctx.send(embed=embed)
    while i < testvalue:
        q = await ctx.send("""**Slot no.{} team {}**""".format(
            i + 1, teamlist[i]))
        try:
            msg = await bot.wait_for('message', timeout=300, check=check)
        except asyncio.TimeoutError:
            await ctx.send(
                "You didn\'t answer in time, please be quicker next time!")
            return
        g = msg.content
        h = g.split(",")
        if len(h) == 5:
            matchplay.append(int(h[0]))
            if int(h[1]) == 1:
                chicken[i] = chicken[i] + 1
                await ctx.send("1 up")
            pospoint1.append(int(h[1]))
            if int(h[3]) == 1:
                chicken[i] = chicken[i] + 1
                await ctx.send("2 up")
            pospoint2.append(int(h[3]))
            killpoint1.append(int(h[2]))
            killpoint2.append(int(h[4]))
            i += 1
        elif g.lower() == "cancel":
            await ctx.send("`Result creation has been cancelled`")
            return
        else:
            embed1 = discord.Embed(
                description=
                "**Values entered in inappropriate manner,try again from start**",
                color=discord.Color(red))
            await ctx.send(embed=embed1)
    totalpoint = []
    killf = []
    posf = []
    i = 0
    pos = [
        0, 15, 12, 10, 8, 6, 4, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0
    ]
    while i < testvalue:
        e = killpoint1[i] + killpoint2[i]
        killf.append(e)
        c = pos[pospoint1[i]] + pos[pospoint2[i]]
        posf.append(c)
        i += 1
    i = 0
    while i < testvalue:
        a = killf[i] + posf[i]
        totalpoint.append(a)
        i += 1
    x = PrettyTable()
    x.field_names = [
        "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
        "Total pts"
    ]
    ntl, nm, nc, np, nk, nt, clone = await pt(ctx, totalpoint, teamlist,
                                              matchplay, chicken, posf, killf,
                                              testvalue)
    ntl, nm, nc, np, nk, nt, ji = await ksort(ntl, nm, nc, np, nk, nt, clone)
    e = 0
    while e < ji:
        x.add_row([(e + 1), ntl[e], nm[e], nc[e], np[e], nk[e], nt[e]])
        e += 1
    embed = discord.Embed(title="Points table",
                          description=x,
                          color=discord.Color(red))
    await ctx.send(embed=embed)
    q = True
    while q:
        await ctx.send(
            "**Choose from the options given below\nTo make chnages to the points of a specific Team type `'1'`\nTo enter record of a new team type `'2'`\nTo save and make the result type `'3'`**"
        )
        try:
            msg = await bot.wait_for("message", timeout=300, check=check)
        except:
            await ctx.send(
                "You didn't answered so the process has been cancelled")
            return
        o = msg.content
        x = """**From the previous points table preview enter the changed data with the unchanged data as entered before in the given format.
      
      **__Format__:-**[Place of team according to the ponints table preview],[Matches played],[Rank in match 1,enter 0 if not played],[Kills in match 1,enter 0 if no kills or not played],[Rank in match 2 , enter 0 if not played],[Kills in match enter 0 if no kills or match not played]**
      
      if not answered in 5 mins the process will automatically be cancelled"""
        c = discord.Embed(title="CORRECTION FORMAT",
                          description=x,
                          color=discord.Color(red))
        if o == "1":
            await ctx.send(embed=c)
            try:
                msg = await bot.wait_for('message', timeout=300, check=check)
            except asyncio.TimeoutError:
                await ctx.send(
                    "You didn\'t answer in time, please be quicker next time!")
                return
            await ctx.send("Details fetched")
            e = msg.content
            lis = e.split(",")
            h = []
            for item in lis:
                h.append(int(item))
            i = 0
            c = 0
            b = int(lis[0]) - 1
            if len(lis) == 6:
                io = True
                while io:
                    if ntl[b] == teamlist[c]:
                        matchplay[c] = h[1]
                        chicken[c] = 0
                        if h[2] == 1:
                            chicken[c] = chicken[c] + 1
                        if h[4] == 1:
                            chicken[c] = chicken[c] + 1
                        posf[c] = pos[h[2]] + pos[h[4]]
                        killf[c] = h[3] + h[5]
                        totalpoint[c] = posf[c] + killf[c]
                        c = 0
                        x = PrettyTable()
                        x.field_names = [
                            "Place", "Team name", "M", "Chicken", "Pos pts",
                            "Kill pts", "Total pts"
                        ]
                        ntl, nm, nc, np, nk, nt, clone = await pt(
                            ctx, totalpoint, teamlist, matchplay, chicken,
                            posf, killf, testvalue)
                        ntl, nm, nc, np, nk, nt, ji = await ksort(
                            ntl, nm, nc, np, nk, nt, clone)
                        i = 0
                        while i < ji:
                            x.add_row([(i + 1), ntl[i], nm[i], nc[i], np[i],
                                       nk[i], nt[i]])
                            i += 1
                        embed = discord.Embed(title="Changed data",
                                              description=x,
                                              color=discord.Color(red))
                        await ctx.send(embed=embed)
                        io = False
                    else:
                        c += 1
            else:
                embed = discord.Embed(
                    description=
                    "**Values entered in inappropriate manner,try again**",
                    color=discord.Color(red))
                await ctx.send(embed=embed)
        elif o == "2":
            testvalue += 1
            ex = [
                "Enter the team name:", "Enter no. of matches played",
                "Enter rank in match 1,type 0 if not played:",
                "Enter no. of kills in match 1:",
                "Enter rank in match 2,enter 0 if not played",
                "Enter no. of kills in match 2"
            ]
            i = 0
            lis = []
            while i < 6:
                await ctx.send("**{}**".format(ex[i]))
                try:
                    msg = await bot.wait_for('message',
                                             timeout=300,
                                             check=check)
                except asyncio.TimeoutError:
                    await ctx.send(
                        "You didn\'t answer in time, please be quicker next time!"
                    )
                    return
                lis.append(msg.content)
                i += 1
            teamlist.append(str(lis[0]))
            ch = 0
            del lis[0]
            matchplay.append(int(lis[0]))
            if lis[1] == 1:
                ch += 1
            if lis[3] == 1:
                ch += 1
            chicken.append(ch)
            posf.append(pos[int(lis[1])] + pos[int(lis[3])])
            killf.append(int(lis[2]) + int(lis[4]))
            totalpoint.append(pos[int(lis[1])] + pos[int(lis[3])] +
                              int(lis[2]) + int(lis[4]))
            x = PrettyTable()
            x.field_names = [
                "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
                "Total pts"
            ]
            ntl, nm, nc, np, nk, nt, clone = await pt(ctx, totalpoint,
                                                      teamlist, matchplay,
                                                      chicken, posf, killf,
                                                      testvalue)
            ntl, nm, nc, np, nk, nt, ji = await ksort(ntl, nm, nc, np, nk, nt,
                                                      clone)
            i = 0
            while i < ji:
                x.add_row([(i + 1), ntl[i], nm[i], nc[i], np[i], nk[i], nt[i]])
                i += 1
            embed = discord.Embed(title="Points table",
                                  description=x,
                                  color=discord.Color(red))
            await ctx.send(embed=embed)
        elif o == "3":
            place1 = []
            while i < testvalue:
                a = 1 + i
                place.append(str(a))
                i += 1
            await sheet(ctx, place1, ntl, nm, nc, np, nk, nt)
            im1 = Image.open('img3.png')
            im2 = Image.open('img2.png')
            mn = testvalue
            await get_concat_v_cut(ctx, im1, im2, mn, ntl, nc, nm, np, nk, nt)
            nl = "\n"
            wtl = ",".join(ntl)
            tor.writelines(wtl + nl)
            wm = ",".join(nm)
            tor.writelines(wm + nl)
            wc = ",".join(nc)
            tor.writelines(wc + nl)
            wp = ",".join(np)
            tor.writelines(wp + nl)
            wk = ",".join(nk)
            tor.writelines(wk + nl)
            wt = ",".join(nt)
            tor.writelines(wt + nl)
            tor.close()
            kl.seek(0)
            days += 1
            j1 = "**T2result**\nDay{}.txt\n{}\nMade by:- {}".format(
                days, poi.strftime("%c"), ctx.author.mention)
            j2 = "Day{}.txt\n{}\n".format(days, poi.strftime("%c"))
            ton.write(j2)
            ton.seek(0)
            lm = "Day{}.txt".format(days)
            cv = ton.read()
            a4 = "t2weekdata/" + lm
            await a2.send(j1, file=discord.File(a4))
            kl.write(str(days))
            ton.close()
            kl.close()
            q = False
        elif o.lower() == "cancel":
            await ctx.send("`Result creation has been cancelled`")
            return
        else:
            l = await ctx.send("**Inappropriate answer.**")
            await asyncio.sleep(5)
            await l.delete()


@t2.error
async def t2_error(ctx, error):
    red = int("ff0000", 16)
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        file = discord.File('asta.gif', filename="image.gif")
        embed = discord.Embed(
            title="ERROR!",
            description=
            "`{}t2 [slotlist]`\n Run the command in the following format".
            format(prefix),
            color=discord.Color(red))
        embed.set_image(url="attachment://image.gif")
        await ctx.send(embed=embed, file=file)
    if isinstance(error, commands.MissingAnyRole):
        embed = discord.Embed(
            description=
            "You must have one of the following roles to use this command:-\n\n1) Result Manager\n2) Result creator",
            color=discord.Color(red))
        await ctx.send(embed=embed)


@bot.command()
async def ret3(ctx):
    await ctx.send("**Upload the txt file**")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=120, check=check)
    except asyncio.TimeoutError:
        print('nhi hyua')
    b = msg.attachments[0]
    if b == "None":
        await ctx.send(
            "NO file attached to the message, process reverted try again")
    await b.save("ret.txt")
    f1 = open("ret.txt", "r")
    i = 0
    while i < 6:
        a1 = f1.readline()
        if i == 0:
            ntl = a1.split(",")
        if i == 1:
            nm = a1.split(",")
        if i == 2:
            nc = a1.split(",")
        if i == 3:
            np = a1.split(",")
        if i == 4:
            nk = a1.split(",")
        if i == 5:
            nt = a1.split(",")
        i += 1
    im1 = Image.open('img1.png')
    im2 = Image.open('img2.png')
    mn = len(ntl)
    await get_concat_v_cut(ctx, im1, im2, mn, ntl, nc, nm, np, nk, nt)
    await ctx.send(file=discord.File("ret.jpg"))


@bot.command()
async def ret2(ctx):
    await ctx.send("**Upload the txt file**")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=120, check=check)
    except asyncio.TimeoutError:
        print('nhi hyua')
    b = msg.attachments[0]
    if b == "None":
        await ctx.send(
            "NO file attached to the message, process reverted try again")
    await b.save("ret.txt")
    f1 = open("ret.txt", "r")
    i = 0
    while i < 6:
        a1 = f1.readline()
        if i == 0:
            ntl = a1.split(",")
        if i == 1:
            nm = a1.split(",")
        if i == 2:
            nc = a1.split(",")
        if i == 3:
            np = a1.split(",")
        if i == 4:
            nk = a1.split(",")
        if i == 5:
            nt = a1.split(",")
        i += 1
    im1 = Image.open('img3.png')
    im2 = Image.open('img2.png')
    mn = len(ntl)
    await get_concat_v_cut(ctx, im1, im2, mn, ntl, nc, nm, np, nk, nt)
    await ctx.send(file=discord.File("ret.jpg"))


#Command fpr reseting days data
@bot.command()
async def rd(ctx):
    await ctx.send(
        "Select from the options given below(one at a time time)\n1) 2-3\n2) T2"
    )
    msg = await time(ctx, bot, 120,
                     "Waited for too long,command has been reverted")
    f1 = msg.content
    f2 = f1.split(",")
    if "1" in f2:
        kl = open("weekdata(2-3)/Days(2-3).txt", "r+")
        a1 = open("weekdata(2-3)/rec.txt", "w")
        kl.write("0")
        kl.seek(0)
        a = kl.read()
        kl.close()
        a1.close()
        await ctx.send("**Days data has been updated to {}**".format(a))
    if "2" in f2:
        pl = open("t2weekdata/Days.txt", "r+")
        a2 = open("t2weekdata/rec.txt", "w")
        pl.write("0")
        pl.seek(0)
        a = pl.read()
        pl.close()
        a2.close()
        await ctx.send("**Days data has been updated to {}**".format(a))
    else:
        await ctx.send("Inappropriate value entered,try again")
        return


bot.run(TOKEN)
