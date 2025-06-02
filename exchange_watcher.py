import asyncio
from config import EXCHANGE_WALLETS
from utils.helius import get_transactions_by_address
from state import fresh_wallets

async def watch_exchange_wallets():
    print("Starting Exchange Wallet Watcher with Helius...")
    while True:
        for exchange_wallet in EXCHANGE_WALLETS:
            txs = get_transactions_by_address(exchange_wallet, limit=10)
            for tx in txs:
                for instruction in tx.get("instructions", []):
                    if instruction.get("type") == "transfer" and instruction.get("program") == "system":
                        recipient = instruction.get("info", {}).get("destination")
                        if recipient and recipient not in fresh_wallets:
                            fresh_wallets.add(recipient)
                            print(f"New fresh wallet funded: {recipient}")
        await asyncio.sleep(30)
