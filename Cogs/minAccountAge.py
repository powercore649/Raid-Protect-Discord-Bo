from Tools.utils import getConfig, updateConfig, getGuildPrefix
import discord
import json

from discord.ext import commands

# ------------------------ COGS ------------------------ #  

class MinAccountAgeCog(commands.Cog, name="commande de modification de l'âge minimum du compte"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'minaccountage', 
                        aliases= ["minage", "agarequired", "age"],
                        usage="<numberInSecond/false>",
                        description="Mettre à jour ou désactiver l'âge minimal du compte pour rejoindre le serveur.")
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 3, commands.BucketType.member)
    @commands.guild_only()
    async def minaccountage(self, ctx, accountAge):

        accountAge = accountAge.lower()

        if accountAge == "false":
            data = getConfig(ctx.guild.id)
            # Add modifications
            data["minAccountDate"] = False
            

            updateConfig(ctx.guild.id, data)

            embed = discord.Embed(title = self.bot.translate.msg(ctx.guild.id, "minAccountAge", "MINIMUM_ACCOUNT_AGE_DISABLED"), description = self.bot.translate.msg(ctx.guild.id, "minAccountAge", "MINIMUM_ACCOUNT_AGE_DISABLED_DESCRIPTION"), color = 0x2fa737) # Green
            await ctx.channel.send(embed = embed)
        else:
            try:
                accountAge = int(accountAge)
                # hour to second
                accountAge *= 3600

                # Edit configuration.json
                data = getConfig(ctx.guild.id)
                # Add modifications
                data["minAccountDate"] = accountAge
                

                updateConfig(ctx.guild.id, data)

                embed = discord.Embed(title = self.bot.translate.msg(ctx.guild.id, "minAccountAge", "MINIMUM_ACCOUNT_AGE_ENABLED"), description = self.bot.translate.msg(ctx.guild.id, "minAccountAge", "MINIMUM_ACCOUNT_AGE_ENABLED_DESCRIPTION"), color = 0x2fa737) # Green
                await ctx.channel.send(embed = embed)

            except:
                prefix = await getGuildPrefix()
                embed = discord.Embed(title=self.bot.translate.msg(ctx.guild.id, "global", "ERROR"), description=self.bot.translate.msg(ctx.guild.id, "minAccountAge", "INVALID_ARGUMENT").format(prefix), color=0xe00000) # Red
                embed.set_footer(text=self.bot.translate.msg(ctx.guild.id, "global", "BOT_CREATOR"))
                return await ctx.channel.send(embed=embed)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(MinAccountAgeCog(bot))
# UPDATE BY OLDMODZ95#3101
# SERVER DISCORD: https://discord.gg/MS6TMgRfqB