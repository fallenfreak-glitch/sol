import requests
from config import TRADEWIZ_BOT_TOKEN, TRADEWIZ_CHAT_ID

def send_to_tradewiz(token_address):
    message = f"/buy {token_address}"
    url = f"https://api.telegram.org/bot{TRADEWIZ_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": TRADEWIZ_CHAT_ID,
        "text": message
    }
    try:
        resp = requests.get(url, params=params, timeout=5)
        if resp.status_code == 200:
            print(f"Sent {token_address} to TradeWiz.")
        else:
            print(f"Failed to send token to TradeWiz: {resp.text}")
    except Exception as e:
        print(f"Exception sending to TradeWiz: {e}")
