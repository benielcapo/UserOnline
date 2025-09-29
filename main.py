import requests

URL_GET_ID = "https://users.roblox.com/v1/usernames/users"
URL_IS_ONLINE = "https://presence.roblox.com/v1/presence/users"
STATUSES = ["offline", "online but not in a game", "online in a game", "in studio"]

def get_user_status(user_id):
    data = {
        "userIds": [user_id]
    }
    response = requests.post(URL_IS_ONLINE, json=data)
    if response.status_code == 200:
        presence_data = response.json()
        presence_data = presence_data["userPresences"][0]
        user_presence = presence_data["userPresenceType"]
        return STATUSES[user_presence] or "unknown"

def get_user_id(username):
    data = {
        "usernames": [username],
        "excludeBannedUsers": True
    }
    response = requests.post(URL_GET_ID, json=data)
    if response.status_code == 200:
        user_data = response.json()
        if user_data["data"]:
            user_id = user_data["data"][0]["id"]
            #print("User ID:", user_id)
            return user_id
    return 0

def get_user_online(username):
    user_id = get_user_id(username)
    if user_id == 0:
        print("failed to fetch user id of " + username)
        return
    status = get_user_status(user_id)
    return status

status = get_user_online("eemessi11")
print("status is: " + str(status))
