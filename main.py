import discord
from dotenv import load_dotenv
import os
import src.pwdlib as pwdlib


# Start of file
pwdlib.initChecks()


TOKEN = pwdlib.getToken()
ScanCommand = pwdlib.parseFromConfig("prefix") + pwdlib.parseFromConfig("scanCommand")

# Init
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    message: discord.Message = message
    mastermessage: discord.Message = message
    
    if message.author.id == client.user.id:
        return
    
    for WhitelistedGuy in pwdlib.parseFromConfig("allowedUserIds"):
        WhitelistedGuy: int = int(WhitelistedGuy)
        if message.author.id == WhitelistedGuy:
            break
    else:
        return

    contents_lowercase: str = message.content.lower()
    
    if contents_lowercase.startswith(ScanCommand):
        await message.reply("Started scanning...", mention_author=False)
        allMembers = set()
        
        # Spooky nested loop!
        for guild in client.guilds:
            print(f"Starting to fetch members from {guild.name}")
            totalForGuild = 0
            guildMembers = await guild.fetch_members()
            for member in guildMembers:
                if member not in allMembers:
                    allMembers.add(member)
                    totalForGuild += 1
                    
            print(f"Got a total of {totalForGuild} for {guild.name}")

        
        
        print(f"Scanned a total of {len(allMembers)} total")
        SpaceWarUsers = 0
        for member in allMembers:
            if not pwdlib.spacewarDetection(member):
                continue
            
            member: discord.Member = member
            SpaceWarUsers += 1
            messageToSend = f"I caught you at {pwdlib.timenow()} playing the game Spacewar which is commonly known for pirating online games. This incident will be logged. Here is a short message:\n{pwdlib.getPirateMessage()}"
            await member.send(messageToSend)
            pwdlib.logPirate(member)
            
        print(f"Done! Found a total of {SpaceWarUsers} Spacewar players")
        await mastermessage.reply(f"Done! Found a total of {SpaceWarUsers} Spacewar players", mention_author=True)



client.run(TOKEN)