import discord
import json
from discord.ext import commands
from Tools.utils import getConfig, updateConfig

# ------------------------ COGS ------------------------ #  

class AntiProfanityCog(commands.Cog, name="change setting from anti nudity command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'antiprofanity', 
                        aliases= ["profanity"],
                        usage="<true/false>",
                        description="Activer ou désactiver l'anti-blasphème.")
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 3, commands.BucketType.member)
    @commands.guild_only()
    async def antiprofanity(self, ctx, antiProfanity):

        antiProfanity = antiProfanity.lower()

        if antiProfanity == "true":
            data = getConfig(ctx.guild.id)
            data["antiProfanity"] = True
            

            embed = discord.Embed(title = self.bot.translate.msg(ctx.guild.id, "profanity", "ANTI_PROFANITY_ENABLED"), description = self.bot.translate.msg(ctx.guild.id, "profanity", "ANTI_PROFANITY_ENABLED_DESCRIPTION"), color = 0x2fa737) # Green
        else:
            data = getConfig(ctx.guild.id)
            data["antiProfanity"] = False
            

            embed = discord.Embed(title = self.bot.translate.msg(ctx.guild.id, "profanity", "ANTI_PROFANITY_ENABLED"), description = self.bot.translate.msg(ctx.guild.id, "profanity", "ANTI_PROFANITY_DISABLED_DESCRIPTION"), color = 0xe00000) # Red
        
        await ctx.channel.send(embed = embed)
        
        updateConfig(ctx.guild.id, data)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(AntiProfanityCog(bot))
# UPDATE BY OLDMODZ95#3101
# SERVER DISCORD: https://discord.gg/MS6TMgRfqB