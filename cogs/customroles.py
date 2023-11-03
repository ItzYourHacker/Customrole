from __future__ import annotations
import discord
from discord.ext import commands
from discord.ext.commands import Context

tick = "<:prime_tick:1165832673785290803>"
cross = "<:cross_hacker:1148075305576177686>"

class custom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.color = 0x000000
     ###################   
     
    @commands.hybrid_command(name="girl", aliases=['girls'], description="Gives girl role to the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def _girls(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT girl, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                girl,reqrole  = data 
                if girl == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Girl Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)

                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=girl) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Girl Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                if Role in user.roles:
                   await user.remove_roles(Role)
                   em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                   em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                   return await ctx.reply(embed=em,delete_after=10)  
                await user.add_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Given {Role.mention} to {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em)                                                
            return None       
                         

    @commands.hybrid_command(name="staff", description="Gives the staff role to the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def _staff(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT staff, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                staff,reqrole  = data 
                if staff == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=staff) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                if Role in user.roles:
                   await user.remove_roles(Role)
                   em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                   em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                   return await ctx.reply(embed=em,delete_after=10)  
                await user.add_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Given {Role.mention} to {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em)                                                
            return None   


    @commands.hybrid_command(name="vip", aliases=['vips'], description="Gives vip role to the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def _vip(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT vip, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                vip,reqrole  = data 
                if vip == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Vip Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=vip) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                if Role in user.roles:
                   await user.remove_roles(Role)
                   em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                   em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                   return await ctx.reply(embed=em,delete_after=10)  
                await user.add_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Given {Role.mention} to {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em)                                                
            return None  
        
        
  
    @commands.hybrid_command(name="guest", aliases=['guests'], description="Gives guest role to the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def _guest(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT guest, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                guest,reqrole  = data 
                if guest == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Guest Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=guest) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                if Role in user.roles:
                   await user.remove_roles(Role)
                   em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                   em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                   return await ctx.reply(embed=em,delete_after=10)  
                await user.add_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Given {Role.mention} to {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em)                                                
            return None  
        
        
                         

    @commands.hybrid_command(name="friend", aliases=['friends'], description="Gives the friend role to the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def _friend(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT friend, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                friend,reqrole  = data 
                if friend == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Friend Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=friend) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Friend Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                if Role in user.roles:
                   await user.remove_roles(Role)
                   em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                   em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                   return await ctx.reply(embed=em,delete_after=10)  
                await user.add_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Given {Role.mention} to {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em)                                                
            return None  
    
####################################################

    @commands.command(aliases=['rstaffs', 'rofficial', 'rofficials'], description="Removes the staff role from the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rstaff(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT staff, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                staff,reqrole  = data 
                if staff == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=staff) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                await user.remove_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em,delete_after=10)                                                
            return None   
  


    @commands.command(aliases=["rvips"], description="Removes the vip role from the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rvip(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT vip, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                vip,reqrole  = data 
                if vip == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=vip) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                await user.remove_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em,delete_after=10)                                            
            return None 

    @commands.command(aliases=['rfriends'], description="Removes the friend role from the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rfriend(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT friend, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                friend,reqrole  = data 
                if friend == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Friend Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=friend) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Friend Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                await user.remove_roles(Role)
                em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=em,delete_after=10)                                                
            return None 
         
   
    @commands.command(aliases=["rguests"], description="Removes the guest role from the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rguest(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT guest, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                guest,reqrole  = data 
                if guest == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Guest Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=guest) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Staff Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                if Role in user.roles:
                   await user.remove_roles(Role)
                   em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                   em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                   await ctx.reply(embed=em,delete_after=10)                                              
            return None  
                     
    @commands.command(aliases=["rgirls"], description="Removes the girls role from the user")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rgirl(self, ctx, user: discord.Member):    
            if user.id == ctx.author.id:
                em = discord.Embed(color=self.color)
                em.set_footer(text="| You can`t change your own roles .",icon_url=ctx.author.display_avatar.url)
                return await ctx.reply(embed=em,delete_after=7)
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT girl, reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Custom roles is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                girl,reqrole  = data 
                if girl == 0:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Girl Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
             
                Rrole = discord.utils.get(ctx.guild.roles, id=reqrole)
                if Rrole is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Reqrole is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)
                
                if ctx.guild.owner.id == ctx.author.id:
                    pass      
                else:
                    if Rrole not in ctx.author.roles:
                        em = discord.Embed(description=f"{cross} You need {Rrole.mention} role to use this command.", color=self.color)
                        em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                        return await ctx.reply(embed=em,delete_after=7) 
                Role = discord.utils.get(ctx.guild.roles, id=girl) 
                if Role is None:
                    em = discord.Embed(color=self.color)
                    em.set_footer(text="| Girl Role is not setuped in this server .",icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7)      
                if Role.position >= ctx.guild.me.top_role.position:
                    em = discord.Embed(description=f"{cross} {Role.mention} is above my top role .", color=self.color)
                    em.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                    return await ctx.reply(embed=em,delete_after=7) 
                if Role in user.roles:
                   await user.remove_roles(Role)
                   em=discord.Embed(description=f"{tick} | Successfully Removed {Role.mention} from {user.mention}", color=self.color)
                   em.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                   return await ctx.reply(embed=em,delete_after=10)                                               
            return None                   
                     
    @commands.hybrid_group(name="setup",
                           description="Setups custom roles for the server .",invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def set(self, ctx: Context):
        prefix=ctx.prefix
        hacker = discord.utils.get(self.bot.users, id=289100850285117460)
        embed = discord.Embed(title=f"Setup", colour=self.color,
                                     description=f"""<...> Duty | [...] Optional\n\n
`{prefix}setup staff <role>` 
Setups girl role for the server .

`{prefix}setup girl <role>`
Setups girl role for the server .

`{prefix}setup friend <role>`
Setups friend role for the server .

`{prefix}setup vip <role>`
Setups vip role for the server .

`{prefix}setup guest <role>`
Setups guest role for the server .

`{prefix}setup reqrole` 
Setups reqrole for customrole commands .

""")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        embed.set_footer(text=f"Made by {hacker.name}" ,  icon_url=hacker.avatar.url)
        await ctx.reply(embed=embed)





    @set.command(name="staff",
                 description="Setups staff role for the server .")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def staff(self, ctx:commands.Context, *, role: discord.Role):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            aliase = 'Staff'
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT staff FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    await cursor.execute("INSERT INTO config (staff , guild ) VALUES (?, ?)",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                
                    await ctx.reply(embed=hacker)
                else:
                    await cursor.execute("UPDATE config SET staff = ? WHERE guild = ?",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                    await ctx.reply(embed=hacker)
                     
            await self.bot.config.commit()        
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=self.color)
            hacker5.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=hacker5)                   
                
            
#######################################################GIRL
    @set.command(name="girl",
                 description="Setups girl role for the server .")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def girl(self, ctx:commands.Context, *, role: discord.Role):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            aliase = 'Girl'
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT girl FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    await cursor.execute("INSERT INTO config (girl , guild ) VALUES (?, ?)",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                
                    await ctx.reply(embed=hacker)
                else:
                    await cursor.execute("UPDATE config SET girl = ? WHERE guild = ?",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                    await ctx.reply(embed=hacker)
                    
            await self.bot.config.commit()        
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=self.color)
            hacker5.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=hacker5)         
            


    @set.command(name="vip",
                 description="Setups vip role for the server .")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def vip(self, ctx:commands.Context, *, role: discord.Role):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            aliase = 'Vip'
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT vip FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    await cursor.execute("INSERT INTO config (vip , guild ) VALUES (?, ?)",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                
                    await ctx.reply(embed=hacker)
                else:
                    await cursor.execute("UPDATE config SET vip = ? WHERE guild = ?",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                    await ctx.reply(embed=hacker)
                    
            await self.bot.config.commit()        
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=self.color)
            hacker5.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=hacker5) 


    @set.command(name="guest",
                 description="Setups guest role for the server .")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def guest(self, ctx:commands.Context, *, role: discord.Role):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            aliase = 'Guest'
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT guest FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    await cursor.execute("INSERT INTO config (guest , guild ) VALUES (?, ?)",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                
                    await ctx.reply(embed=hacker)
                else:
                    await cursor.execute("UPDATE config SET guest = ? WHERE guild = ?",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                    await ctx.reply(embed=hacker)
                    
                    
            await self.bot.config.commit()        
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=self.color)
            hacker5.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=hacker5) 


    @set.command(name="friend",
                 description="Setups friend role for the server .")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def friend(self, ctx:commands.Context, *, role: discord.Role):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            aliase = 'Friend'
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT friend FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    await cursor.execute("INSERT INTO config (friend , guild ) VALUES (?, ?)",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                
                    await ctx.reply(embed=hacker)
                else:
                    await cursor.execute("UPDATE config SET friend = ? WHERE guild = ?",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Custom aliase {aliase.capitalize()} is set to {role.mention}\nJust type `{aliase.lower()} <member>` to give or `r{aliase.lower()} <member>` to take {role.mention} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                    await ctx.reply(embed=hacker)
                    
                     
            await self.bot.config.commit()        
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=self.color)
            hacker5.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=hacker5) 
            
            
            

    @set.command(name="reqrole",
                 description="setup reqrole for custom role commands .",
                 aliases=['r'])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def reqrole(self, ctx:commands.Context, *, role: discord.Role):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            async with self.bot.config.cursor() as cursor:
                await cursor.execute("SELECT reqrole FROM config WHERE guild = ?",(ctx.guild.id,))
                data = await cursor.fetchone()
                if not data:
                    await cursor.execute("INSERT INTO config (reqrole , guild ) VALUES (?, ?)",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Reqiured role to run custom role commands is set to {role.mention} For {ctx.guild.name} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                    await ctx.reply(embed=hacker)
                else:
                    await cursor.execute("UPDATE config SET reqrole = ? WHERE guild = ?",(role.id,ctx.guild.id,))
                    hacker = discord.Embed(
                     description=
                     f"{tick} | Reqiured role to run custom role commands is set to {role.mention} For {ctx.guild.name} .",
                    color=self.color)
                    hacker.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
                    hacker.set_thumbnail(url=ctx.author.display_avatar.url)
                    await ctx.reply(embed=hacker)  
            await self.bot.config.commit()        
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=self.color)
            hacker5.set_author(name=ctx.author.display_name,
                               icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=hacker5) 
            
    @set.command(name="config", description="Shows the current custom role settings for the server")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.guild_only()
    async def config(self, context:commands.Context):
        async with self.bot.config.cursor() as cursor:
            await cursor.execute("SELECT reqrole , staff , friend , vip , guest , girl FROM config WHERE guild = ?",(context.guild.id,))
            data = await cursor.fetchone()
            if not data:
                hacker = discord.Embed(
                     description=
                     f"{cross} | First setup Your required role by Running `{context.prefix}setup reqrole @role/id` .",
                    color=self.color)
                hacker.set_author(name=context.author.display_name,
                               icon_url=context.author.display_avatar.url)
                return await context.reply(embed=hacker)  
            reqrole , staff , friend , vip , guest , girl = data 
            
            if staff !=0:
                stafff = discord.utils.get(context.guild.roles, id=staff)
                staffr = stafff.mention
            else:
                staffr = "Staff role is not set"
            if girl != 0:
                girll = discord.utils.get(context.guild.roles, id=girl)
                girlr = girll.mention
            else:
                girlr = "Girl role is not set"
            if vip != 0:
                vipp = discord.utils.get(context.guild.roles, id=vip)
                vipr = vipp.mention
            else:
                vipr = "Vip role is not set"
            if guest != 0:
                guestt = discord.utils.get(context.guild.roles, id=guest)
                guestr = guestt.mention
            else:
                guestr = "Guest role is not set"
            if friend != 0:
                frndr = discord.utils.get(context.guild.roles, id=friend)
                frndr = frndr.mention
            else:
                frndr = "Friend role is not set"
            if reqrole != 0:
                reqrole = discord.utils.get(context.guild.roles, id=reqrole)
                reqr = reqrole.mention
            else:
                reqr = "Req role is not set"


            embed = discord.Embed(
                title=f"Custom roles Settings For {context.guild.name}",
                color=self.color)
            embed.add_field(
                name="Req Role:",
                value=f"{reqr}",
                inline=False)
            embed.add_field(
                name="Staff Role:",
                value=f"{staffr}",
                inline=False)
            embed.add_field(
                name="Girl Role:",
                value=f"{girlr}",
                inline=False)
            embed.add_field(name="Vip Role:",
                            value=f"{vipr}",
                            inline=False)
            embed.add_field(
                name="Guest Role:",
                value=f"{guestr}",
                inline=False)
            embed.add_field(
                name="Friend Role:",
                value=f"{frndr}",
                inline=False)
            embed.set_thumbnail(url =context.author.display_avatar.url)  
            return await context.send(embed=embed)          
        
        
async def setup(bot):
    await bot.add_cog(custom(bot))