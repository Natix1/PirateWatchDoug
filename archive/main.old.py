import discord
from dotenv import load_dotenv
import os

alreadycaughtnotifier = "ALREADY-CAUGHT-IGNORE"
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

allowed_user_id = 955090007335530506
# user id allowed to use the bots $startscan

# Obtain the discord token from the .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("Please enter a valid token in the .env file")
    
# Init
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('$startscan') or message.content.startswith("s"):
        if message.author.id != allowed_user_id:
            # ignore
            return
        
        masterchannel = message.channel
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
                            dm_channel = await member.create_dm()
                            messages = [message async for message in dm_channel.history(limit=100)]
                            

                            alreadycaught = False 


                            for message in messages:                
                                if alreadycaughtnotifier in message.content:
                                    # detected pirate but for preventing spam no message
                                    print(f'Message found: {message.content}')
                                    alreadycaught = True

                                      

                            # detected pirate
                            if not alreadycaught:
                                await member.send(antipiratemessage)
                                await member.send(alreadycaughtnotifier)
                                await masterchannel.send(f"Detected pirate: {member.name}")
                                print(f"Detected pirate: {member.name}")
                                with open("hallofpirates.txt", "a") as f:
                                    f.write(f"{member.name} | {member.id} | 1\n")
                            else:
                                with open("hallofpirates.txt", "r") as f:
                                    lines = f.readlines()

                                for i, line in enumerate(lines):
                                    if str(member.id) in line:
                                        split_line = line.split("|")
                                        count = int(split_line[2]) + 1
                                        split_line[2] = str(count)
                                        lines[i] = "|".join(split_line)
                                        break
                                    
                                with open("hallofpirates.txt", "w") as f:
                                    f.writelines(lines)
                                            

                                print(f"Detected but was already caught earlier: {member.name}")
                                await masterchannel.send(f"Detected pirate that was already caught earlier: {member.name}")

                    processed_members.append(member)



client.run(TOKEN)