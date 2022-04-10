import requests
import helper

config = helper.read_config()

channel_id = config["Pokebot"]["channel_id"]

authorization = config["Pokebot"]["authorization"]


def send_message(payload):
    headers = {"authorization": authorization}
    r = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        data=payload,
        headers=headers,
    )


def clear_message():

    payload = {"content": "?purge 50"}
    headers = {"authorization": authorization}
    r = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        data=payload,
        headers=headers,
    )


def hint_message():

    payload = {"content": "p!hint"}
    headers = {"authorization": authorization}
    r = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        data=payload,
        headers=headers,
    )
