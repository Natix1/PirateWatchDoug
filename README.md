# Pirate Scanner Bot

This selfbot scans all servers using `discord-py-self`, looking for users playing the game "Spacewar." If it finds any, it flags them as pirates and logs them in a file named `hallofpirates.txt` with the format:

```
NAME | USER ID | HOW MANY TIMES
```

The bot also includes a protection mechanism to prevent spamming users multiple times.

## Disclaimer
**This is a selfbot and violates Discord's Terms of Service (TOS). It is for educational purposes only. Use at your own risk.**

Running this bot may cause disruption to other users or servers, and I am **not** responsible for any damage caused by its usage, no matter how severe. **Do not use this bot irresponsibly.** 

Also, if a thermonuclear war breaks out because of this bot, I’ve warned you!

## Setup Guide

1. Clone this repository and navigate into the directory:
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. Create a file named `.env` in the root directory and add your Discord token:
   ```env
   TOKEN=<your-discord-token>
   ```
   You can find tutorials online on how to obtain your token.

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the bot:
   ```bash
   python src/main.py
   ```

6. The first time you run the bot, it will generate a `config.json` file in the `src/` folder. Open `config.json` and add your Discord user ID under the `allowedUserIds` section.

7. Sit back, relax, and wait... the scan may take several hours, depending on how many servers you’re in.

If you don’t know how to do any of the above, **do your own research**.
