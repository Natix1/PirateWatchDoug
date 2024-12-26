import discord
from dotenv import load_dotenv
import os


antipiratemessage = """
Yo, so like, pirating is totally not the vibe, fam. 
It's lowkey stealing and messes up the game for devs who worked hard, ya know? 
If you're out here downloading sketchy stuff, you're risking your device, too. 
Like, you don't wanna catch a virus or get your account hacked, right? 
Plus, it's straight-up illegal, bro, and we don’t need that smoke. 
Just support the creators, buy the thing, and keep it 100. 
Don’t be a pirate, be a good homie.
https://tenor.com/view/hop-on-spacewar-spacewar-hop-on-hop-space-gif-15791507099589222017
https://tenor.com/view/memories-gif-21184195
ᵗʰᶦˢ ᵐᵉˢˢᵃᵍᵉ ʷᵃˢ ᵃᵘᵗᵒᵐᵃᵗᶦᶜᵃˡˡʸ ᵃⁿᵈ ᵖʳᵒᵍʳᵃᵐᵃᵗᶦᶜᵃˡˡʸ ˢᵉⁿᵗ ᵇʸ ᴾᶦʳᵃᵗᵉᵂᵃᵗᶜʰᴰᵒᵘᵍ
"""


# Obtain the discord token from the .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("Please enter a valid token in the .env file")

# TODO
# 1. Fetch all server lists
# 2. Fetch all members in every server
# 3. Fetch every members activity

# Init
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('$startscan') or message.content.startswith("s"):
        await message.channel.send('Starting scan...')
        guilds = client.guilds

        processed_members = []

        for guild in guilds:
            # print(f"Guild name: {guild.name}")

            
            for guild in guilds:
                guild_members = guild.members
                for member in guild_members:
                    if member in processed_members:
                        continue
                    member_activities = member.activities
                    # print(f"{(member.name).upper()} has the following activities: {member_activities}")
                    
                    for activity in member_activities:
                        if not isinstance(activity, discord.Game):
                            continue

                        if activity.name == "Spacewar":
                            # detected pirate
                            await member.send(antipiratemessage)
                            await message.channel.send(f"Detected pirate: {member.name}")
                            print(f"Detected pirate: {member.name}")

                    processed_members.append(member)



client.run(TOKEN)