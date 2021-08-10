# Discord Recon Backend
# InviteEngine.py 
# Objective: To find various information about a discord server with nothing but an invite link

import requests
import json

def InvRecon(invite):
    res = requests.get("https://discord.com/api/v9/invites/" + str(invite))
    data = res.json()
    try:
        server_id = data["guild"]["id"]
    except:
        return 0
    server_name = data["guild"]["name"]
    server_veri_level = data["guild"]["verification_level"]
    server_nsfw_level = data["guild"]["nsfw"]
    server_vanity = data["guild"]["vanity_url_code"]
    try:
        server_welcome_message = data["guild"]["welcome_screen"]["description"]
    except:
        server_welcome_message = "None"
    try:
        inviter_user_id = data["inviter"]["id"]
        inviter_username = data["inviter"]["username"]
        inviter_discriminator = data["inviter"]["discriminator"]
        inviter_avatar = data["inviter"]["avatar"]
    except:
        inviter_user_id= "None"
        inviter_username= "None"
        inviter_discriminator= "None"
        inviter_avatar="None"
    serverInfo = [server_id, server_name, server_veri_level, server_nsfw_level, server_vanity, server_welcome_message, inviter_user_id, inviter_username, inviter_discriminator, inviter_avatar]
    return serverInfo
