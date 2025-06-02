import asyncio
from db.blacklist import is_blacklisted
from utils.rate_limiter import can_trigger
from utils.pumpfun import is_token_on_pumpfun
from db.models import log_trade
from tradewiz.notifier import send_to_tradewiz
from utils.helius import get_token_mints_by_address
from state import fresh_wallets

async def watch_mints():
    print("Starting Mint Watcher with Pump.fun suffix logic...")
    while True:
        for wallet in list(fresh_wallets):
            mints = get_token_mints_by_address(wallet, limit=5)
            for mint in mints:
                token_address = mint.get("mint")
                deployer = mint.get("authority") or mint.get("owner")

                if not token_address or not deployer:
                    continue

                if is_blacklisted(deployer):
                    print(f"Skipping blacklisted deployer {deployer}")
                    continue

                if not can_trigger(deployer, cooldown=300):
                    print(f"Cooldown active for deployer {deployer}")
                    continue

                if is_token_on_pumpfun(token_address):
                    send_to_tradewiz(token_address)
                    log_trade(token_address, deployer, wallet)
                    print(f"✅ Token {token_address} from {deployer} sent to TradeWiz and logged.")
                else:
                    print(f"❌ Token {token_address} is not a Pump.fun mint.")
        
        await asyncio.sleep(15)
