import asyncio
from prettytable import PrettyTable
import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import re
import datetime
import os
import xlsxwriter
from myfunc import *
#Global variables:-
red = int("ff0000", 16)
dg = int("ADE6B2", 16)
pos = [0, 15, 12, 10, 8, 6, 4, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0]


async def res(ctx,bot,a):
  n1=f"{ctx.author.id}/rec.txt"
  f1=open(n1,"r")
  fd1=f1.readlines()
  lc1=len(fd1)
  f1.close()
  p = re.compile('Team.*')
  rawlist = p.findall(a)
  testvalue = len(rawlist)
  teamlist = []
  nt=[]
  nk = []
  nm = []
  np = []
  nc = []
  i = 0
  while i < testvalue:
    nc.append(0)
    i += 1
  for item in rawlist:
    rie = item.replace("Team", "")
    teamlist.append(rie)
  if len(teamlist) < 3:
    await ctx.send("Improper data entered, process has been cancelled try again")
    return
  i = 0
  a ="""**Now enter the records of the team asked. 5 mins will be given for each entry. Enter `cancel` for quiting the process.**"""
  embed = discord.Embed(title=f"MATCH NO. {lc1+1}",description=a,color=discord.Color(red))
  embed.set_footer(text="MONKEY D. LUFFY")
  await ctx.send(embed=embed)
  pos = [0, 15, 12, 10, 8, 6, 4, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0]
  while i < testvalue:
    a1= """**Slot no.{} team {}**""".format(i + 3, teamlist[i])
    embed=discord.Embed(description=a1,color=discord.Color(red))
    q = await ctx.send(embed=embed)
    e=0
    embed1=discord.Embed(description=a1,color=discord.Color(red))
    a1=["Enter 1 if team played the match else enter 0 :-","Enter the rank of team :-","Enter kills scored by the team:-"]
    while e<3:
      await ctx.send("**{}**".format(a1[e]))
      msg=await time(ctx,bot,300,"You took an year to answer, process has bee terminated. Try again")
      if e==0 and msg.content=="0":
        i+=1
        nm.append(0)
        np.append(0)
        nk.append(0)
        nt.append(0)
        embed1.add_field(name="Match played",value=0,inline=True)
        embed1.add_field(name="Place pts.",value=0,inline=True)
        embed1.add_field(name="Kill pts.",value=0,inline=True)
        await q.edit(embed=embed1)
        break
      elif e==0and msg.content=="1":
        nm.append(1)
        e+=1
        embed1.add_field(name="Match played",value=msg.content,inline=True)
      elif e==1 :
        np.append(pos[int(msg.content)])
        if msg.content=="1":
          nc[i]=1
        e+=1
        embed1.add_field(name="Place pts.",value=pos[int(msg.content)],inline=True)
      elif e==2:
        nk.append(int(msg.content))
        nt.append(nk[i]+np[i])
        embed1.add_field(name="Kill pts.",value=int(msg.content),inline=True)
        e+=1
        await q.edit(embed=embed1)
        i+=1
      elif msg.content.lower() == "cancel":
        await ctx.send("`Result creation has been cancelled`")
        return
      else:
        embed1 = discord.Embed(description="**Values entered in inappropriate manner,try again from start**",color=discord.Color(red))
        await ctx.send(embed=embed1)
  x = PrettyTable()
  x.field_names = [
        "Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts",
        "Total pts"]
  i = 0
  e = 0
  ntl=teamlist.copy()
  clone = nt.copy()
  clone.sort(reverse=True)
  elist = []
  ftl = []
  fm = []
  fp = []
  fk = []
  ft = []
  fc = []
  while i < testvalue:
    if e in elist:
        e += 1
    else:
      if nt[e] == clone[i]:
        ftl.append(ntl[e])
        fm.append(nm[e])
        fp.append(np[e])
        fk.append(nk[e])
        ft.append(nt[e])
        fc.append(nc[e])
        i += 1
        elist.append(e)
        e = 0
      else:
        e += 1
  ftl,fm,fc,fp,fk,ft,ji = await ksort(ftl,fm,fc,fp,fk,ft,clone)
  e = 0
  while e < ji:
    x.add_row([(e + 1), ftl[e], fm[e], fc[e], fp[e], fk[e], ft[e]])
    e += 1
  embed = discord.Embed(title="Points table",
                  description=x,color=discord.Color(red))
  await ctx.send(embed=embed)
  q = True
  while q:
    await ctx.send("**Choose from the options given below\nTo make chnages to the points of a specific Team type `'1'`\nTo save and make the result type `'2'`**")
    msg=await time(ctx,bot,300,"Didn't answered on time , process has been reverted")
    o = msg.content
    x = """**Enter the asked details,5mins are given for each entry.**"""
    c = discord.Embed(title="CORRECTION FORMAT",description=x,color=discord.Color(red))
    embed.set_footer(
            text=
            "if not answered in 5 mins the process will automatically be cancelled"
        )
    if o == "1":
      await ctx.send(embed=c)
      e=0
      a1=["Enter the current position of the team given in the points table above :-","Enter 1 if team played the match else enter 0 :-","Enter the rank of team :-","Enter kills scored by the team:-"]
      while e<4:
        await ctx.send("**{}**".format(a1[e]))
        msg= await time(ctx,bot,300,"Didn't answered in time the process has been reverted")
        if e==0:
          if 0>int(msg.content)>testvalue:
            await ctx.send("Enter the exact position of the team.")
            break
          else:
            a=int(msg.content)-1
            e+=1
        elif e==1:
          if int(msg.content)==0:
            fm[a]=int(msg.content)
            fp[a]=0
            fk[a]=0
            break
          elif int(msg.content)==1:
            fm[a]=int(msg.content)
            e+=1
          else:
            await ctx.send("Answer shoul be eithrt 0 or 1")
        elif e==2:
          fp[a]=pos[int(msg.content)]
          e+=1
        elif e==3:
          fk[a]=int(msg.content)
          ft[a]=fp[a]+fk[a]
          e+=1
        elif msg.content.lower()=="cancel":
          await ctx.send("Process has been reverted")
          return
      ntl=ftl.copy()
      nm=fm.copy()
      nc=fc.copy()
      np=fp.copy()
      nk=fk.copy()
      nt=ft.copy()
      x = PrettyTable()
      x.field_names = ["Place", "Team name", "M", "Chicken", "Pos pts", "Kill pts","Total pts"]
      i = 0
      e = 0
      clone = ft.copy()
      clone.sort(reverse=True)
      elist = []
      ftl = []
      fm = []
      fp = []
      fk = []
      ft = []
      fc = []
      while i < testvalue:
        if e in elist:
          e += 1
        else:
          if nt[e] == clone[i]:
            ftl.append(ntl[e])
            fm.append(nm[e])
            fp.append(np[e])
            fk.append(nk[e])
            ft.append(nt[e])
            fc.append(nc[e])
            i += 1
            elist.append(e)
            e = 0
          else:
            e += 1
      ftl,fm,fc,fp,fk,ft,ji = await ksort(ftl,fm,fc,fp,fk,ft,clone)
      e = 0
      while e < ji:
        x.add_row([(e + 1), ftl[e], fm[e], fc[e], fp[e], fk[e], ft[e]])
        e += 1
      embed = discord.Embed(title="Points table",
                      description=x,color=discord.Color(red))
      await ctx.send(embed=embed)
    elif o == "2":
      await ctx.send("**Enter the match no.\n (enter 2 digits number only if its 2 enter 02)**")
      msg= await time(ctx,bot,300,"Didn't answer in time process has been reverted")
      man=msg.content
      place1 = []
      while i < testvalue:
        a = 1 + i
        place.append(str(a))
        i += 1
      await sheet(ctx, place1, ftl, fm, fc, fp, fk, ft)
      im=Image.open("vggcres.png")
      mio = await ctx.send("**Started entering Team records**")
      font2 = ImageFont.truetype("fonts/Lemonb.otf",60)
      font1 = ImageFont.truetype("fonts/Lemonb.otf",30)
      font = ImageFont.truetype("fonts/Landm.otf",50)
      a = [140,230,585,660,715,790,880,1000,1100,1455,1530,1610,1680,1760]
      ko=[400,453,506,559,612,665,718,771,824,877,400,453,506,559,612,665,718,771,824,877]
      col=(255,255,255)
      i=0
      d=ImageDraw.Draw(im)
      draw=d.text((1077,66),man,col,font=font2)
      mn=len(ftl)
      if mn>20:
        mn=20
      while i<10:
        draw = d.text((a[0], ko[i]), str(i+1), col, font=font1)
        draw = d.text((a[1], ko[i]), str(ftl[i]),col, font=font)
        draw = d.text((a[2], ko[i]), str(fc[i]), col, font=font1)
        draw = d.text((a[3], ko[i]), str(fm[i]), col, font=font1)
        draw = d.text((a[4], ko[i]), str(fp[i]), col, font=font1)
        draw = d.text((a[5], ko[i]), str(fk[i]), col, font=font1)
        draw = d.text((a[6], ko[i]), str(ft[i]), col, font=font1)
        await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(ftl[i]))
        i+=1
      while 9<i<mn:
        draw = d.text((a[7], ko[i]), str(i+1), col, font=font1)
        draw = d.text((a[8], ko[i]), str(ftl[i]),col, font=font)
        draw = d.text((a[9], ko[i]), str(fc[i]), col, font=font1)
        draw = d.text((a[10], ko[i]), str(fm[i]), col, font=font1)
        draw = d.text((a[11], ko[i]), str(fp[i]), col, font=font1)
        draw = d.text((a[12], ko[i]), str(fk[i]), col, font=font1)
        draw = d.text((a[13], ko[i]), str(ft[i]), col, font=font1)
        await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(ftl[i]))
        i+=1
      im.save("res.png")
      await mio.edit(content="**Successfully entered all the records <a:emoji_55:856633188485955584>,uploading the file**")
      await ctx.send(file=discord.File("res.png"))
      fn2=f"{ctx.author.id}/match{lc1+1}.txt"
      tor=open(fn2,"w")
      nm,nc,np,nk,nt=list(map(str,fm)),list(map(str,fc)),list(map(str,fp)),list(map(str,fk)),list(map(str,ft))
      nl = "\n"
      wtl = ",".join(ftl)
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
      poi = await it()
      n1=f"{ctx.author.id}/rec.txt"
      f1=open(n1,"a+")
      j2 = "match{}.txt|{}\n".format(lc1+1, poi.strftime("%c"))
      f1.write(j2)
      a1=ctx.guild.channels
      a2 = discord.utils.get(a1, name="points-table-data")
      j1 = "**Match{}.txt\n{}\nMade by:- {} **".format(lc1+1, poi.strftime("%c"), ctx.author.mention)
      await a2.send(j1,file=discord.File(fn2))
      q=False
    elif o.lower()== "cancel":
      await ctx.send("Process has been revertd")
      return
    else:
      await ctx.send("Enter a valid option")

async def restt(ctx,bot):
  f1 = open(f"{ctx.author.id}/rec.txt", "r")
  a = f1.readlines()
  a1=len(a)
  if a1 == 0:
    embed = discord.Embed(title="NO FILE FOUND",
            description=
            "No files present in the directory, create point tables or upload data record files in order to make the Weekly result",
            color=discord.Color(red))
    await ctx.send(embed=embed)
    return
  i = 0
  embed = discord.Embed(title="DATA RECORD",
        description=
        "Select Days whose data is to be processed further in the following format.\n n,n,n,....\n`{n represents the no. of day}`",
        color=discord.Color(red))
  z=0
  f1.seek(0)
  while z<a1:
    a2=f1.readline()
    a3=a2.split("|")
    embed.add_field(name=a3[0],value=a3[1])
    z+=1
  await ctx.send(embed=embed)
  msg=await time(ctx,bot,180,'**You took too long to reply. Process has been cancelled ,try again**')
  if str(msg.content.lower()) == "cancel":
    await ctx.send("`Result making process has been cancelled`")
    return
  a = (msg.content).split(",")
  t = len(a)
  b = "{}/match{}.txt".format(ctx.author.id,a[0])
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
      mp1=wp.copy()
      i += 1
    elif i == 4:
      f = d.split(",")
      wk = list(map(int, f))
      mk1=wk.copy()
      i += 1
    elif i == 5:
      f = d.split(",")
      wt = list(map(int, f))
      i += 1
  a1=len(wtl)
  r=0
  dic={}
  while r<a1:
    dic[wtl[r]]=[wp[r],wk[r]]
    r+=1
  d1=dic
  i = 1
  while i < t:
    aio = "{}/match{}.txt".format(ctx.author.id,a[i])
    f3 = open(aio, "r")
    ntl = []
    nm = []
    nc = []
    np = []
    nk = []
    nt = []
    e = 0
    while e < 6:
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
    dic={}
    while e < c:
      if ntll[e] in wtll:
        d = wtll.index(ntll[e])
        wm[d] = wm[d] + nm[e]
        wc[d] = wc[d] + nc[e]
        wp[d] = wp[d] + np[e]
        wk[d] = wk[d] + nk[e]
        wt[d] = wt[d] + nt[e]
        dic[ntl[e]]=[np[e],nk[e]]
        e += 1
      else:
        wtl.append(ntl[e])
        wm.append(nm[e])
        wc.append(nc[e])
        wp.append(np[e])
        wk.append(nk[e])
        wt.append(nt[e])
        dic[ntl[e]]=[np[e],nk[e]]
        e += 1
    if i==1:
      d2=dic
    if i==2:
      d3=dic
    if i==3:
      d4=dic
    if i==4:
      d5=dic
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
        ftl.append((wtl[e]))
        fm.append((wm[e]))
        fc.append((wc[e]))
        fp.append((wp[e]))
        fk.append((wk[e]))
        ft.append((wt[e]))
        i += 1
        elist.append(e)
        e = 0
      else:
        e += 1
  ftl,fm,fc,fp,fk,ft,ji = await ksort(ftl,fm,fc,fp,fk,ft,clone)
  print(fk)
  i=0
  f1.close()
  await ctx.send("Enter no.")
  place1=[]
  mn=len(ftl)
  while i<mn:
    place1.append(str(i+1))
    i+=1
  msg=await time(ctx,bot,300,"Took to long to respond. Process has been reverted")
  await sheet(ctx, place1, ftl, fm, fc, fp, fk, ft)
  man=msg.content
  nm,nc,np,nk,nt=list(map(str,fm)),list(map(str,fc)),list(map(str,fp)),list(map(str,fk)),list(map(str,ft))
  im=Image.open("vggcres.png")
  mio = await ctx.send("**Started entering Team records**")
  font2 = ImageFont.truetype("fonts/Lemonb.otf",60)
  font1 = ImageFont.truetype("fonts/Lemonb.otf",30)
  font = ImageFont.truetype("fonts/Landm.otf",50)
  a = [140,230,585,660,715,790,880,1000,1100,1455,1530,1610,1680,1760]
  ko=[400,453,506,559,612,665,718,771,824,877,400,453,506,559,612,665,718,771,824,877]
  col=(255,255,255)
  i=0
  d=ImageDraw.Draw(im)
  draw=d.text((1077,66),man,col,font=font2)
  print(ftl)
  if mn>20:
    mn=20
  while i<10:
    draw = d.text((a[0], ko[i]), str(i+1), col, font=font1)
    draw = d.text((a[1], ko[i]), ftl[i],col, font=font)
    draw = d.text((a[2], ko[i]), nc[i], col, font=font1)       
    draw = d.text((a[3], ko[i]), nm[i], col, font=font1)
    draw = d.text((a[4], ko[i]), np[i], col, font=font1)
    draw = d.text((a[5], ko[i]), nk[i], col, font=font1)
    draw = d.text((a[6], ko[i]), nt[i], col, font=font1)
    await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(ftl[i]))
    i+=1
  while 9<i<mn:
    draw = d.text((a[7], ko[i]), str(i+1), col, font=font1)
    draw = d.text((a[8], ko[i]), ftl[i],col, font=font)
    draw = d.text((a[9], ko[i]), nc[i], col, font=font1)
    draw = d.text((a[10], ko[i]),nm[i], col, font=font1)
    draw = d.text((a[11], ko[i]),np[i], col, font=font1)
    draw = d.text((a[12], ko[i]),nk[i], col, font=font1)
    draw = d.text((a[13], ko[i]), nt[i], col, font=font1)
    await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(ftl[i]))
    i+=1
  im.save("res.png")
  fn2=f"{man}.txt"
  tor=open(fn2,"w")
  nl = "\n"
  wtl = ",".join(ftl)
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
  a1=ctx.guild.channels
  poi=await it()
  a2 = discord.utils.get(a1, name="points-table-data")
  j1 = "**Compiled data:- {}.txt\n{}\nMade by:- {} **".format(man, poi.strftime("%c"), ctx.author.mention)
  await a2.send(j1,file=discord.File(fn2))
  os.remove(fn2)
  await mio.edit(content="**Successfully entered all the records <a:emoji_55:856633188485955584>,uploading the file**")
  await ctx.send(file=discord.File("res.png"))
async def vgret(ctx):
  f1 = open("restu.txt", "r")
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
  im=Image.open("vggcres.png")
  mio = await ctx.send("**Started entering Team records**")
  font2 = ImageFont.truetype("fonts/Lemonb.otf",60)
  font1 = ImageFont.truetype("fonts/Lemonb.otf",30)
  font = ImageFont.truetype("fonts/Landm.otf",50)
  a = [140,230,585,660,715,790,880,1000,1100,1455,1530,1610,1680,1760]
  ko=[400,453,506,559,612,665,718,771,824,877,400,453,506,559,612,665,718,771,824,877]
  col=(255,255,255)
  i=0
  d=ImageDraw.Draw(im)
  d=ImageDraw.Draw(im)
  man="01-03"
  draw=d.text((1077,66),man,col,font=font2)
  mn=len(ntl)
  print(ntl)
  while i<10:
    draw = d.text((a[0], ko[i]), str(i+1), col, font=font1)
    draw = d.text((a[1], ko[i]), ntl[i],col, font=font)
    draw = d.text((a[2], ko[i]), nc[i], col, font=font1)       
    draw = d.text((a[3], ko[i]), nm[i], col, font=font1)
    draw = d.text((a[4], ko[i]), np[i], col, font=font1)
    draw = d.text((a[5], ko[i]), nk[i], col, font=font1)
    draw = d.text((a[6], ko[i]), nt[i], col, font=font1)
    await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(ntl[i]))
    i+=1
  while 9<i<20:
    draw = d.text((a[7], ko[i]), str(i+1), col, font=font1)
    draw = d.text((a[8], ko[i]), ntl[i],col, font=font)
    draw = d.text((a[9], ko[i]), nc[i], col, font=font1)
    draw = d.text((a[10], ko[i]),nm[i], col, font=font1)
    draw = d.text((a[11], ko[i]),np[i], col, font=font1)
    draw = d.text((a[12], ko[i]),nk[i], col, font=font1)
    draw = d.text((a[13], ko[i]), nt[i], col, font=font1)
    await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(ntl[i]))
    i+=1
  im.save("res.png")
  await mio.edit(content="**Successfully entered all the records <a:emoji_55:856633188485955584>,uploading the file**")
  await ctx.send(file=discord.File("res.png"))