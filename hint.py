import requests


def hint_message():

    payload = {"content": "p!hint"}
    header = {
        "authorization": ""
    }
    r = requests.post(
        "",
        data=payload,
        headers=header,
    )
