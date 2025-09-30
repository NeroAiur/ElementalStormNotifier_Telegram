from json import load, dump
import pathlib
import shutil

print("This is the setup tool for the Elemental Storm Notifier\n")
print("NOTICE: This is the Telegram version, if you wanted the Discord version, please head to the Link below:")
print("https://github.com/NeroAiur/ElementalStormNotifier_Discord")
print("----------------------------------------------------------\n\n")
print("First off, please choose whether you are on EU [1] or US [2] servers")
region = input(">>> ")

print("\nPlease provide your Bot Token (get it from BotFather - look in the README.md if you don't know how)")
bot_token = input(">>> ")

print("\nNow please provide your Chat ID (get it from @userinfobot - look in the README.md if you don't know how)")
chat_id = input(">>> ")

with open("assets/config.json", "r+") as f:
    data = load(f)
    
    data["region"] = "EU" if region == "1" else "US"
    data["platform"] = "telegram"
    data["bot_token"] = bot_token
    data["chat_id"] = chat_id
    
    f.seek(0)
    dump(data, f, indent=4)
    f.truncate()
print("\nConfig file setup complete: assets/config.json")

path = str(pathlib.Path().resolve()) + "/"
shutil.move(path + "src/run.bat", path + "run.bat")
shutil.move(path + "src/run.sh", path + "run.sh")

print("\nSetup complete, you can now run the script with `python main.py`")
print("To create a repetetive task, please look into the README.md file")
print("You can now delete the setup.py file if you want.")
print("Happy Storm Hunting!")
input()