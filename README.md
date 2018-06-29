# Installation
  - To install this test bot, clone this repo in your local directory.
```
cd ~/path/to/local/repo
git clone https://gitlab.com/noktyn/jr-test-bot.git
```
  - It is recommended to use a `virtualenv` with all python projects. You can do that with the following commands:
```
virtualenv ~/path/to/virtualenv/different/from/local/repo
cd ~/path/to/local/repo
source ~/path/to/virtualenv/different/from/local/repo/bin/activate
```
**NOTE:** The "/bin/" path may be "/Scripts/" depending on your OS/setup for `virtualenv`.
  - Lastly, you'll need to create main/dist.py file and store your client token in there. There is  main/dist_example.py file demonstrating where it goes as far as configuration.


# Starting the bot
First, the bot will need to join the Discord server. You can do that using the following URL after creating your bot:
  - *https://discordapp.com/oauth2/authorize?client_id=<CLIENT_ID>&scope=bot*
  - This will open a page that allows you to select the Discord server to join based on the account you're logged into on the Discord developer page. Once the bot has joined the server, it will most likely appear offline.

Next, we need to make the bot connect and actually be able to process commands. Simply open a command prompt or terminal and run the client.py script as is from this repo. The bot should connect and all of the commands should work.

# Commands list
**WIP**
  - **!test:**: Calculates the user's messages for the channel they called "!test" in. Limits to 100.
  - **!sleep:** Sleeps the bot for 5 seconds.
  - **!update:** Sends text "Update test." to chat.
