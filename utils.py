import requests
from config import HELIUS_API_KEY, HELIUS_BASE_URL

HEADERS = {
    "Content-Type": "application/json",
    "api-key": HELIUS_API_KEY
}

def get_transactions_by_address(address, limit=10):
    url = f"{HELIUS_BASE_URL}/addresses/{address}/transactions"
    params = {
        "limit": limit
    }
    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Helius API error for {address}: {e}")
        return []

def get_token_mints_by_address(address, limit=10):
    url = f"{HELIUS_BASE_URL}/addresses/{address}/mints"
    params = {
        "limit": limit
    }
    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Helius API error for mints {address}: {e}")
        return []
