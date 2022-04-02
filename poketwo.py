import requests
import json
import time


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
        username = value["author"]["username"]
        attachment = value["attachments"]
        if "The pokmon is" in content:
            print("Hint")
        elif bool(attachment):
            print("Pokemon")


while True:
    retrieve_messages(channel_id)
    time.sleep(10)
