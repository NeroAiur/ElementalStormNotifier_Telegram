def main():
    import scrape
    import parse
    import telegram
    import asyncio
    import time
    
    zone = "Unknown"
    element = ""
    remaining_time = ""
    

    while zone == "Unknown":
        html = scrape.scrape_webpage("https://www.wowhead.com/wow/retail")
        active_storms = parse.parse_html(html)
        zone = active_storms[0][0]
        
        # If no Zone is yet revealed, retry in 5 minutes
        if zone == "Unknown":
            print("No Results Found - Retrying in 5 Minutes!")
            time.sleep(300)
    
    API_token = "7055579736:AAEEBxOU_qiU5fExaIKg4vd9PSXlVP1OJco"
    cID = -1002001951674

    # this fixes the code to not wait long enough for the bot response
    async def send(msg, chat_ID, token=API_token):
        bot = telegram.Bot(token=token)
        await bot.sendMessage(chat_id=chat_ID, text=msg)
        print("Message Sent!")
        
    message = "Elemental Storm Tracker - Currently Active Storms"
    
    for storm in active_storms:
        zone = storm[0]
        element = storm[1]
        remaining_time = storm[2]
        
        # add special paraphrase if the last one I need is up
        if zone == "Thaldraszus" and element == "Fire":
            message = message + "LAST NEEDED ELEMENTAL STORM"
            
        message = message + """
            Zone: {zone}
            Element: {element}
            Time Remaining: {time_remaining}
            """.format(zone=zone, element=element, time_remaining=remaining_time)
    
    asyncio.run(send(msg=message, chat_ID=cID, token=API_token))

if __name__ == "__main__":
    main()