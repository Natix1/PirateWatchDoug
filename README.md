It scans thru all servers by using discord-py.self. Looks for activities. If any user is playing spacewar blame him for being a pirate. Add to a file called hallofpirates.txt with this format:  
NAME | USER ID | HOW MANY TIMES  
Includes protection against spamming people multiple times.  
I'm sorry for anyone reviewing this code. Total mess.  
If I am every gonna work on this again I am making sure to split this up into multiple files and functions.  
For now enjoy.  
### Note a scan might take days if your client is in multiple big servers. No joke.
DISCLAIMER THIS IS A SELFBOT. AGAINST DISCORD TOS. EDUCATIONAL PURPOSES ONLY. MAKE SURE TO RUN ONLY WHEN YOU ARE CERTAIN YOU CAUSE NO HARM TO ANYONE!!! I AM NOT RESPONSIBLE FOR ANY DAMAGE YOU CAUSE WITH THIS, NO MATTER THE SEVERITY.
AGAIN, I DO NOT CARE (but still go ahead and create an issue) IF A THERMONUCLEAR WAR BREAKS OUT BECAUSE OF THIS. I WARNED YOU.
# setup guide
1. Clone this repo & CD into it
2. Create a file in that directory with the name '.env'
3. Put this: `TOKEN=` alongside your discord token. Tutorials how to find online.
4. Create a virtual environment
5. Install dependencies as listed in requirements.txt
6. Run python src/main.py
7. Adjust config.json and put your user-id inside the allowedUserIds (config.json) is created automatically in src/ after running main.py without it
8. Enjoy waiting hours for the scans to finish
If you do not know how to do the above, you can do your own research
