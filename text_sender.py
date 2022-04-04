import requests


def send_message(payload):

    header = {
        "authorization": ""
    }
    r = requests.post(
        "",
        data=payload,
        headers=header,
    )
