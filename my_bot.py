import discord

TOKEN = 'NDQ0ODU0NDY3NDY1MTgzMjMy.Ddh-4A.R6MrWzUAebDAostZxS3TymoOZUo'

client = discord.Client()

server = client.get_server('439468629734588429')

import sys

@client.event
async def on_message(message):
    # dont want the bot to reply to itself
    if message.author == client.user:
        return

    if discord.Server.id != '439468629734588429':
        sys.exit

    #rcv is the received message variable
    #this make coding much easier
    #also the messages are no longer case sensitive
    rcv = str.lower(message.content)
    aut = message.author.id

    corrac = '$accept' #this is a script that will detect new users and give them a role to see the rest of the channels if they accept
    if message.channel.id == '445203736747573249' and rcv == corrac :
        msg = "Welcome to SHEEPY's server and thank you for accepting our rules. You (should) have the member role now and should be able to see more channels."
        await client.send_message(message.channel, msg)
    elif message.channel.id == '445203736747573249' and rcv != corrac :
        msg = "Oops, looks like you've made a typo. Please type $accept if you accept the rules."
        await client.send_message(message.channel, msg)

    if 'you are mum gay' in rcv :
        msg = 'no u' .format(message)
        await client.send_message(message.channel, msg)

    if '$big gay' in rcv :
        msg = 'il est tres big gay' .format(message)
        await client.send_message(message.channel, msg)

    if '$does it work' in rcv :
        msg = 'Yes {0.author.mention}, yes it does!' .format(message)
        await client.send_message(message.channel, msg)

    if '$does it finally work' in rcv :
        msg = 'Yes {0.author.mention}, yes it finally works!' .format(message)
        await client.send_message(message.channel, msg)

    if 'sheepy bot is genius' in rcv :
        msg = 'Glad you think so {0.author.mention}!' .format(message)
        await client.send_message(message.channel, msg)

    if '$hello' in rcv :
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if '$hi' in rcv :
        msg = 'Sup {0.author.mention}!' .format(message)
        await client.send_message(message.channel, msg)

    if 'vtec' in rcv :
        msg = 'DID I HEAR VTEC? NEROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOWM' .format(message)
        await client.send_message(message.channel, msg)

    if  'gay' in rcv :
        msg = 'Is that homophobia I hear? reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
        await  client.send_message(message.channel, msg)

@client.event
async def on_member_join(member) :
    msg = member
    await client.send_message(discord.Client.Server.Channel.id('439724121811714068'), msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print ('have a nice day boi')
    print('------')
client.run(TOKEN)