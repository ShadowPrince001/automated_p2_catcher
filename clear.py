import requests


def clear_message():

    payload = {"content": "?purge 10"}
    header = {
        "authorization": ""
    }
    r = requests.post(
        "",
        data=payload,
        headers=header,
    )

