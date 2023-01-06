from PIL import *
import asyncio
from prettytable import PrettyTable
import discord
from discord.ext import commands
from io import BytesIO
import re
import datetime
import xlsxwriter
import os

async def it():
  poi= datetime.datetime.now() + datetime.timedelta(hours=5,minutes=30)
  return poi
async def td(message):
    a=message.content.lower()
    r2=re.compile("\d+h")
    r3=re.compile("\d+m")
    r4=re.compile("\d+s")
    h1=r2.findall(a)
    m1=r3.findall(a)
    s1=r4.findall(a)
    if len(h1)>0:
      h1=h1[0].replace("h","")
    else:
      h1=0
    if len(m1)>0:
      m1=m1[0].replace("m","")
    else:
      m1=0
    if len(s1)>0:
      s1=s1[0].replace("s","")
    else:
      s1=0
    try:
      h= int(h1)
      m=int(m1)
      s=int(s1)
    except:
      return True
    x=datetime.timedelta(hours=h,minutes=m, seconds=s)
    return x                                                                                                                                                          
  
async def cembed(ctx,color,description,title):
  if title==None:
    embed=discord.Embed(description=description,timestamp=datetime.datetime.utcnow(),color=discord.Color(color))
  else:
    embed=discord.Embed(title=title,description=description,timestamp=datetime.datetime.utcnow(),color=discord.Color(color))
  await ctx.send(embed=embed)


async def get_concat_v_cut(ctx,im1, im2,mn,ntl,nm,nc,np,nk,nt):
  i=0
  mio = await ctx.send("**Started entering Team records**")
  dst = Image.new('RGB', (im2.width, (im1.height+mn*im2.height)))
  dst.paste(im1,(0,0))
  font1 = ImageFont.truetype("fonts/Lemonb.otf",200)
  font = ImageFont.truetype("fonts/Landm.otf",300)
  a = [240,500,2500,2900,3500,4030,4550]
  im2.close()
  ko=100
  while i<mn:
    im2 = Image.open('img2.png') 
    d=ImageDraw.Draw(im2)
    draw = d.text((a[0], ko), str(i+1), (0, 0, 0), font=font1)
    draw = d.text((a[1], ko), ntl[i],(0, 0, 0), font=font)
    draw = d.text((a[2], ko), nc[i], (0, 0,0), font=font1)
    draw = d.text((a[3], ko), nm[i], (0, 0,0), font=font1)
    draw = d.text((a[4], ko), np[i], (0, 0,0), font=font1)
    draw = d.text((a[5], ko), nk[i], (0, 0,0), font=font1)
    draw = d.text((a[6], ko), nt[i], (0,0,0), font=font1)
    dst.paste(im2, (0,(im1.height + i*im2.height)))
    await mio.edit(content="**Data of team {} has been successfully entered <a:emoji_55:856633188485955584> **".format(ntl[i]))
    im2.close()
    i+=1
  dst.save("res.jpg")
  await mio.edit(content="**Successfully entered all the records <a:emoji_55:856633188485955584>,uploading the file**")
  await ctx.send(file=discord.File("res.jpg"))

async def ksort(ntl,nm,nc,np,nk,nt,clone):
  q = True
  ji=len(ntl)
  i=0
  fk=list(map(int,nk))
  while q==True:
    if i==ji-1:
      q=False
    elif clone[i]==clone[i+1]:
      print("cauth one")
      if fk[i]<fk[i+1]:
        c1,c2,c3,c4,c5,c6=ntl[i],nm[i],nc[i],np[i],nk[i],nt[i]
        c11,c12,c13,c14,c15,c16=ntl[i+1],nm[i+1],nc[i+1],np[i+1],nk[i+1],nt[i+1]
        ntl[i],nm[i],nc[i],np[i],nk[i],nt[i]=c11,c12,c13,c14,c15,c16
        ntl[i+1],nm[i+1],nc[i+1],np[i+1],nk[i+1],nt[i+1]=c1,c2,c3,c4,c5,c6
        c18,c19=fk[i],fk[i+1]
        fk[i],fk[i+1]=c19,c18
        i=0
        print("ksorted one")
      else:
        i+=1
    else:
      i+=1
  return ntl,nm,nc,np,nk,nt,ji


async def time(ctx,bot,time,reason):
  print("sarted")
  def check(m):
    return m.author == ctx.author and m.channel == ctx.channel
  try:
    msg= await bot.wait_for('message',timeout=time,check=check)
  except asyncio.TimeoutError:
    await ctx.send(reason)
    return
  return msg
async def sheet(ctx,place,ntl,nm,nc,np,nk,nt):
  workbook = xlsxwriter.Workbook('Pointstable.xlsx')
  worksheet = workbook.add_worksheet()
  titles  = ["Place","Team name","M","Chicken","Pos pts","Kill pts","Total pts"]
  worksheet.write_row(0, 0,titles)
  worksheet.write_column(1,0,place)
  worksheet.write_column(1,1,ntl)
  worksheet.write_column(1,2,nm)
  worksheet.write_column(1,3,nc)
  worksheet.write_column(1,4,np)
  worksheet.write_column(1,5,nk)
  worksheet.write_column(1,6,nt)
  workbook.close()
  await ctx.send(file =discord.File("Pointstable.xlsx"))
async def pt(ctx,totalpoint,teamlist,matchplay,chicken,posf,killf,testvalue):
  clone = totalpoint.copy()
  clone.sort(reverse=True)
  i = 0 
  e = 0
  elist=[]
  ntl = []
  nm = []
  np =[]
  nk =[]
  nt = []
  nc=[]
  while i < testvalue:
    if e in elist:
      e+=1
    else:
      if totalpoint[e]==clone[i]:
        ntl.append(str(teamlist[e]))
        nm.append(str(matchplay[e]))
        np.append(str(posf[e]))
        nk.append(str(killf[e]))
        nt.append(str(totalpoint[e]))
        nc.append(str(chicken[e]))
        i += 1
        elist.append(e)
        e=0
      else:
        e+=1
  return ntl,nm,nc,np,nk,nt,clone
