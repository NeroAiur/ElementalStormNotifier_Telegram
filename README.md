# wowhead_storm_scraper
This project came from my absolute lazyness that I did not want to open my webbrowser every 3 hours to look up which Elemental Storm is active... So yes, this script does look up what storm currently is active...

**THIS IS THE TELEGRAM-VERSION**\
Link to the Discord Version:\
https://github.com/NeroAiur/ElementalStormNotifier_Discord


# Requirements
- Python 3.8 or higher
#### Libraries:
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pythong-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- [chromedriver_autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/)
- [selenium](https://pypi.org/project/selenium/)

to install all the nessecary libraries execute the following command:\
`python -m pip install beautifulsoup4 python-telegram-bot chromedriver-autoinstaller selenium`

# Setup
Execute the setup script ´setup.py´. You will need the following to complete the configuration:
* Telegram Bot API-Token
* Telegram Bot Target Chat ID

To learn how to create a telegram bot click [here](https://core.telegram.org/bots/tutorial) to get to the official Telegram guide on bots. There you will also find your API-Key

You can get the ID of the target Chat by forwarding a message from the target chat to [@jsonDumpBot](https://t.me/JsonDumpBot). This bot wil reply a json dump which also holds the ID of the channel.

You can also edit the message headers and bodys to your liking, for that just head to the assets/config.json file and edit any of the "message_*" attributes.

# How to Automize
### Windows
* open the Windows Task Scheduler by pressing `Win + R` and typing `taskschd.msc`
* head to `Action` and click `create task`
* name your task whatever you wish
* head to `Trigger` and click `New`
* Choose `Once` and choose your current date at `00:05:00` (5min after the full hour because of potential delays)
* make it repeat **every three hours** and click `OK`
* head to `Actions` and click `New`
* enter the path to the `run.bat` file and click `OK`
* click `OK` again
* done

### Linux
* type crontab -e
* at the very end of the file add the following: `5 */3 * * * sh /path/to/run.sh` (5min after the full hour because of potential delays)
* press `CTRL + S` and `CTRL + X`
* done
