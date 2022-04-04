import requests
import json
import time
from text_sender import send_message
from clear import clear_message
from pokemon_list import pokemon_list
from hint import hint_message

channel_id = "956528701175124041"


def retrieve_messages(channel_id):
    headers = {
        "authorization": "mfa.yZiDpjSp50M0Uv_B4zBOtkreV8ZU6mTscky4y9r7X-3N58e1t1bPAGAud5CsBtMD6SltqkrsVwPQv67BlVBr"
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
            print(content)
            slc = slice(15, -1)
            content = content[slc]
            print(content)
            content = content.replace("\\", "")
            print(content)
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
                        payload = {"content": a}
                        send_message(payload)
                        counter = 0
                        clear_message()
                    else:
                        counter = 0

        elif bool(embed) or bool(attachment):
            clear_message()

            hint_message()


while True:
    retrieve_messages("956528701175124041")
    time.sleep(10)
