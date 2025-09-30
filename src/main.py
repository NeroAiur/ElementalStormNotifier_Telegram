def main():
    import json
    import scrape
    import parse
    import telegram
    import asyncio
    import time
    
    # defining asynchronous function, this is nessecary, because the code has to await
    # the response of the telegram bot, otherwise it will result in errors
    async def send(msg, chat_ID, token):
        bot = telegram.Bot(token=token)
        await bot.sendMessage(chat_id=chat_ID, text=msg)
        print("Message Sent!")
    
    # loading config file
    with open("assets\\config.json") as f:
        config = json.load(f)
        
    # getting messaging-configs from config
    API_token = config["Telegram-API-token"]
    cID = config["Telegram-Target-Chat"]
    
    zone = "Unknown"    # this is integrated to emulate a do-while-loop
    while zone == "Unknown":
        html = scrape.scrape_webpage("https://www.wowhead.com/wow/retail")
        active_storms = parse.parse_html(html)
        
        # simple error handling, if the region is not correctly set to "EU" or "US",
        # it will send out an Error message to the designated Telegram Chat
        if active_storms == -1:
            message = config["message-header-error"] + config["message-body-error-config-error"]
            asyncio.run(send(msg=message, chat_ID=cID, token=API_token))
            
            return -1
        
        zone = active_storms[0][0]
        
        # If no Zone is yet revealed, retry in 5 minutes
        if zone == "Unknown":
            print("No Results Found - Retrying in 5 Minutes!")
            time.sleep(300)
    
    message = config["message-header"]
    
    for storm in active_storms:
        zone = storm[0]
        element = storm[1]
        remaining_time = storm[2]
        
        # add special line if a needed storm is up (WIP to have it be configurable)
        if zone == "Thaldraszus" and element == "Fire":
            message = message + config["message-body-storm-needed"]
            
        message = message + config["message-body"].format(zone=zone, element=element, time_remaining=remaining_time)
    
    asyncio.run(send(msg=message, chat_ID=cID, token=API_token))
    
    return 0

if __name__ == "__main__":
    main()