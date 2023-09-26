import discord
from requests import post
import base64
import json

from discord import SyncWebhook, Colour
from datetime import datetime

class Discord:
    def __init__(self) -> None:
        self.webhook_url = "https://discord.com/api/webhooks/1156281048171294761/vGwwxrH28OOwwKisWtSsfuWmKlFXWU4HShGRQU-d6PZ1Rp6ZO5v6jbUkYtQr03dOE2Av"

    def send_webhook(self, message_description: str) -> None:
        # Create webhook from url
        webhook = SyncWebhook.from_url(self.webhook_url)

        # Embed message to send
        embed = discord.Embed(
            title="Spotify Info",
            description=message_description,
            colour=Colour.red(),
            timestamp=datetime.now()
        )

        # Send payload to webhook url
        webhook.send(embed=embed)

# Spotify Client ID and Secret (Would never post in code would use env variable or some key management host)
client_id = ""
client_secret = ""
    
def get_access_token():
    # Build authorization string
    authorization_string = client_id + ":" + client_secret
    authorization_bytes = authorization_string.encode('utf-8')
    authorization_base64 = str(base64.b64encode(authorization_bytes), 'utf-8')

    # Build payload to send
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + authorization_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # Send payload and retrieve access token
    query = post(token_url, headers=headers, data=data)
    json_data = json.loads(query.content)
    access_token = json_data["access_token"]

    return access_token

# Get access token
access_token = get_access_token()

# Send token to discord
discord_bot = Discord()
discord_bot.send_webhook(access_token)