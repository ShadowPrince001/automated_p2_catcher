import requests
import json
import time
import helper
from text_sender import send_message, clear_message, hint_message
from pokemon_list import pokemon_list

config = helper.read_config()

channel_id = config["Pokebot"]["channel_id"]

authorization = config["Pokebot"]["authorization"]

catch_rate = config["Pokebot"]["catch_rate"]

catch_rate = int(catch_rate)


def retrieve_messages(channel_id):
    headers = {"authorization": authorization}
    r = requests.get(
        f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers
    )
    jsonn = json.loads(r.text)
    for value in jsonn:
        content = value["content"]
        usercontent = value["author"]["username"]
        attachment = value["attachments"]
        embed = value["embeds"]
        if "The pokémon is " in content:
            content = content.replace("\\", "")
            length = len(content)
            slc = slice(15, length)
            content = content[slc]
            length = len(content)
            count = 0
            for x in content:
                if (x.isalpha()) == True or x == "-" or x == "'":
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
    retrieve_messages(channel_id)
    time.sleep(catch_rate)
