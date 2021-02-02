# ts3-alertbot
[![version](https://img.shields.io/badge/version-1.0-fff12f?style=for-the-badge)](https://github.com/zile42O/ts3-alertbot)

## What is this?
- This is a bot that notifies clients on the server that a DDoS attack is in progress.
## How it works?
- The bot script sends a request to a specific interval on its own API that is on the same virtual server as the bot and teamspeak server, and then that API processes that request and sends the bot, the number in MB, which is directed to the VPS of 100 mb / s the bot notifies that a DDoS attack is in progress, if the attack stops the bot will notify after a certain interval that the attack has been stopped.
## Requirements
- TeamSpeak 3 Server
- Python
- Ts3 Python Libary
## Setup
- Put the layer4.php in your web space (example: var/www/html) before that install apache and other required tools
- Create Server query login (Username, Password), and fill the required information in the main.py file
- Save main.py file
- Install/Import python ts3 libary
- Start your Ts3 Bot with command:  
```bash
 python3 main.py
```
## Note
- Currently the layer4.php file was not originally used before, I made it quickly and it should be worked on, also the most important thing to change the current calculation is in Byte, change to MB!
