import requests
import json


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
        username = value["author"]["username"]
        attachment = value["attachments"]
        if "The pokémon is" in content:
            print("Hint")
        elif attachment != 0:
            print("Pokemon")


retrieve_messages("")
