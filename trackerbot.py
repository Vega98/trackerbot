import telegram
import requests
from time import sleep

trackers: list = [
    {"url": "<URL of webpage you want to track", "search" : "<Words you want to change in the page>", "name" : "<Name of webpage>", "flagged": "false"
    #...you can add as many pages as you want   
]

# VARIABLES
# headers variable is needed to bypass webpages that stop GET requests without browser info, usually done to stop bots like this one

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
api_key = "<This is your telegram bot api key>"
user_id = "<Your personal telegram user_id>"
status_message: str = "Webpage {0} {1} {2}"
chat_message: str = "Hey! The webpage {0} was updated! {1}"
err_message: str = "Error occured fetching {0}: {1}"

# TELEGRAM BOT INITIALIZATION

bot = telegram.Bot(token=api_key)

while True:
    for tracker in trackers:

        #try to find specified string in specified url

        try:
            response = requests.get(tracker["url"], headers=headers)
            if response.status_code != 200:
                print(err_message.format(tracker["name"], response.status_code))
                continue

            if tracker["search"] in response.text
                    #I found the "sorry, closed" mark on this page, logging can be disabled by commenting next line
                    print(status_message.format(tracker["name"], "not updated", ""))
            elif tracker["flagged"] == "true":
                #avoid spamming messages if already sent one, logging can be disabled by commenting next line
                print(tracker["name"]+" was updated, but I already told you!")
            else:
                #send telegram message, logging can be disabled by commenting next line
                print(status_message.format(tracker["name"], "WAS UPDATED!", tracker["url"]))
                bot.send_message(chat_id=user_id, text=chat_message.format(tracker["name"], tracker["url"]))
                tracker["flagged"] = "true"


        except Exception as ex:
			#Exception logging, uncomment second line if you wish to receive a telegram message too
            print(f"Error occured fetching {tracker['name']}: {ex}")
            #bot.send_message(chat_id=user_id, text="Error occured fetching {tracker['name']}: {ex}")

    print("Cycle finished. Waiting 1 minute to start again...")
    sleep(60)
