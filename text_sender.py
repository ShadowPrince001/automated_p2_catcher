import requests


def send_message(payload):

    header = {
        "authorization": "mfa.yZiDpjSp50M0Uv_B4zBOtkreV8ZU6mTscky4y9r7X-3N58e1t1bPAGAud5CsBtMD6SltqkrsVwPQv67BlVBr"
    }
    r = requests.post(
        "https://discord.com/api/v9/channels/956528701175124041/messages",
        data=payload,
        headers=header,
    )
