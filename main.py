import requests
import json
import time
from text_sender import send_message
from clear import clear_message
from pokemon_list import pokemon_list
from hint import hint_message

channel_id = ""

def retrieve_messages(channel_id):
    headers = {
        "authorization": ""
    }
    r = requests.get(
        f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers
    )
    jsonn = json.loads(r.text)
    for value in jsonn:
        content = value["content"]
        usercontent = value["author"]["username"]
        attachment = value["attachments"]
        embed = value["embeds"]
        if "The pokémon is" in content:
            slc = slice(15, -1)
            content = content[slc]
            content = content.replace("\\", "")
            length = len(content)
            count = 0
            for x in content:
                if (x.isalpha()) == True:
                    count += 1
            counter = 0
            for a in pokemon_list:
                if length == len(a):
                    for r in range(length):
                        if content[r] is a[r]:
                            counter += 1
                    if counter == count:
                        print(a)
                        a = "p!c " + a
                        time.sleep(1)
                        payload = {"content": a}
                        send_message(payload)
                        counter = 0
                        time.sleep(1)
                        clear_message()
                    else:
                        counter = 0

        elif bool(embed) or bool(attachment):
            time.sleep(1)
            clear_message()
            time.sleep(1)
            hint_message()
   
            

while True:
    retrieve_messages("")
    time.sleep(5)
