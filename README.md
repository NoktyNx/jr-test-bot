# Installation
  - To install this test bot, clone this repo in your local directory.
```
cd ~/path/to/local/repo
git clone https://github.com/NoktyNx/jr-test-bot.git
```
  - It is recommended to use a `virtualenv` with all python projects. You can do that with the following commands:
```
virtualenv ~/path/to/virtualenv/different/from/local/repo
cd ~/path/to/local/repo
source ~/path/to/virtualenv/different/from/local/repo/bin/activate
```
**NOTE:** The `/bin/` path may be `/Scripts/` depending on your OS/setup for `virtualenv`.
  - Lastly, you'll need to create main/dist.py file and store your client token in there. There is  main/dist_example.py file demonstrating where it goes as far as configuration.


# Starting the bot
First, the bot will need to join the Discord server. You can do that using the following URL after creating your bot (replace CLIENT_ID with your bot's client ID):
  - *https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot*
  - This will open a page that allows you to select the Discord server to join based on the account you're logged into on the Discord developer page. Once the bot has joined the server, it will most likely appear offline.

Next, we need to make the bot connect and actually be able to process commands. Simply open a command prompt or terminal and run the main/launcher.py script as is from this repo. The bot should connect and all of the commands should work. Launch commands are as follows (include the "" for the Windows command):

**Windows (in command prompt):**
`"~repo/directory/main/launcher.py"`

**Mac:**
`.~/repo/directory/main/launcher.py`


# Commands list
**WIP**
  - **!classes:** Displays how to use the class command and the available options.
  - **!classes Barbarian:** Displays Barbarian class information. Replace "Barbarian" with class class listed from the !class command.
  - **/roll:** Enables the rolling of dice. Example: "/roll 1d6" rolls one six sided dice.
  - **etc.** More commands will be documented in this matter as the DND bot is built.
