# wowhead_storm_scraper
This project came from my absolute lazyness that I did not want to open my webbrowser every 3 hours to look up which Elemental Storm is active... So yes, this script does look up what storm currently is active... the repetition is realised with Windows Task Scheduler

# Requirements
- Python 3.8 or higher
> Libraries:
> - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
> - [pythong-telegram-bot](https://pypi.org/project/python-telegram-bot/)
> - [chromedriver_autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/)
> - [selenium](https://pypi.org/project/selenium/)\
> \
> to install the libraries execute the following command\
> \
> `python -m pip install beautifulsoup4 python-telegram-bot chromedriver-autoinstaller selenium`

# Configuration
The following things need to be configured:
* region
* Telegram Bot API-Token
* Telegram Bot Target Chat ID

You can do this in the `config.json` file found in the `assets` directory

The `region` attribute has to be either "EU" or "US", depending in which region you are in.

The `Telegram-API-token` attribute holds the API-key of your Telegram bot. To learn how to create such a bot click [here](https://core.telegram.org/bots/tutorial) to get to the official Telegram guide on bots.

The `Telegram-Target-Chat` attribute holds the ID of the chat you wish to post your message in. You can get this ID by forwarding a message from the target chat to [@jsonDumpBot](https://t.me/JsonDumpBot). This bot wil reply a json dump which also holds the ID of your channel.

You can also edit the message headers and bodys to your liking.

# To-Do
* custom "you still need this storm" implementation
* setup batch to create a scheduled task in windows
