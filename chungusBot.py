import discord
import chungusBotCommands


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    async def on_ready(self):

        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message):

        args = message.content.split()
        args = [element.strip() for element in args]
        user = message.author

        # Things to be printed to the console for testing.
        print('User is: ', user, '\nMention is: ', user.mention, '\nUser name: ', user.name, '\nUser ID is: ', user.id,
              '\nChannel is: ', message.channel, '\nChannel ID: ', message.channel.id, '\nUser groups', user.roles, '\n')

        if message.author == self.user:

            return

        # $help expects no arguments, returns a discord rich embed with all commands.
        if message.content.startswith('$help'):

            helpEmbed = discord.Embed(type='rich', title='Command List',
                                      description='A list of commands and their arguments. Use a space to seperate arguments and commands. Ex. $example username2 stuffandthings')

            await message.channel.send(embed=helpEmbed)

        if 'chungus' in message.content.lower():

            await message.edit(content='Chungus punishment message.')
            await user.edit(nick='Chungus Abuser')
            await user.add_roles('ChungusAbuserRole', reason='Chungus Abuser')
            await message.channel.send('Chungus Abuser Found!')


if __name__ == '__main__':

    token = ''

    with open('apiKey.txt') as file:

        token = file.read()

    client = MyClient()
    client.run(token)
