import discord
from discord.ext import commands
from Tools.utils import getGuildPrefix

# ------------------------ COGS ------------------------ #  

class HelpCog(commands.Cog, name="help command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'help',
                        usage="(commandName)",
                        description = "Display the help message.")
    @commands.cooldown(1, 3, commands.BucketType.member)
    async def help(self, ctx, commandName=None):

        commandName2 = None
        stop = False

        if commandName is not None:
            for i in self.bot.commands:
                if i.name == commandName.lower():
                    commandName2 = i
                    break 
                else:
                    for j in i.aliases:
                        if j == commandName.lower():
                            commandName2 = i
                            stop = True
                            break
                if stop:
                    break 

            if commandName2 is None:
                await ctx.channel.send("No command found!")   
            else:
                embed = discord.Embed(title=f"**{commandName2.name.upper()} COMMAND :**", description="[**Serveur Discord**](https://discord.gg/MS6TMgRfqB)", color=0xdeaa0c)
                embed.set_thumbnail(url=f'{self.bot.user.avatar_url}')
                embed.add_field(name=f"**NAME :**", value=f"{commandName2.name}", inline=False)
                aliases = ""
                if len(commandName2.aliases) > 0:
                    for aliase in commandName2.aliases:
                        aliases = aliase
                else:
                    commandName2.aliases = None
                    aliases = None
                embed.add_field(name=f"**ALIASES :**", value=f"{aliases}", inline=False)
                if commandName2.usage is None:
                    commandName2.usage = ""
                    
                prefix = await getGuildPrefix(self.bot, ctx)
                embed.add_field(name=f"**USAGE :**", value=f"{prefix}{commandName2.name} {commandName2.usage}", inline=False)
                embed.add_field(name=f"**DESCRIPTION :**", value=f"{commandName2.description}", inline=False)
                embed.set_footer(text="Développer par OldModz95#3105")
                await ctx.channel.send(embed=embed)
        else:
            prefix = await getGuildPrefix(self.bot, ctx)
            embed = discord.Embed(title=f"__**Pas d'aide {self.bot.user.name.upper()}**__", description="[**Serveur Discord**](https://discord.gg/MS6TMgRfqB)\n\n**{prefix}help (command) :**Afficher la liste d'aide ou les données d'aide pour une commande spécifique.", color=0xdeaa0c)
            embed.set_thumbnail(url=f'{self.bot.user.avatar_url}')
            embed.add_field(name=f"__ADMIN :__", value=f"**{prefix}setup <on/off> :** Setup la protection captcha.\n**{prefix}settings :** Afficher la liste des paramètres.\n**{prefix}giveroleaftercaptcha <role ID/off> :** Ajoute un role après avoir passer le captcha.\n**{prefix}minaccountage <number (hours)> :** Ajoute une limite d'age du compte pour passer le captcha (24 heures par défaut).\n**{prefix}antinudity <true/false> :** Auto-protection des images de nudité.\n**{prefix}antiprofanity <true/false> :** Activer ou désactiver la protection contre les grossièretés.\n**{prefix}antispam <true/false> :** Activer ou désactiver la protection anti-spam.\n**{prefix}allowspam <#channel> (remove) :** Activer ou désactiver la protection anti-spam dans un canal spécifique.\n**{prefix}lock | unlock <#channel/ID> :**Bloquer/Débloquer un channel.\n\n**{prefix}kick <@user/ID> :** Ejecter un utilisateur.\n**{prefix}ban <@user/ID> :** ban un utilisateur.\n\n**{prefix}changeprefix <prefix> :** Changez le prefix du bot.\n**{prefix}changelanguage <fr-FR/en-US> :** Changer le langage du bot.", inline=False)
            embed.add_field(name=f"__COMMANDES :__", value=f"**{prefix}userinfos <@user/ID> :** Voir les informations d'un utilisateur.", inline=False)
            embed.set_footer(text="Développer par OldModz95#3105")
            await ctx.channel.send(embed=embed)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.remove_command("help")
    bot.add_cog(HelpCog(bot))
# UPDATE BY OLDMODZ95#3101
# SERVER DISCORD: https://discord.gg/MS6TMgRfqB