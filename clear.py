import requests


def clear_message():

    payload = {"content": "?purge 50"}
    header = {
        "authorization": ""
    }
    r = requests.post(
        "",
        data=payload,
        headers=header,
    )

