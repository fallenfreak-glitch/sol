import asyncio
from db.models import init_db
from tracker.exchange_watcher import watch_exchange_wallets
from tracker.mint_watcher import watch_mints

async def main():
    init_db()
    await asyncio.gather(
        watch_exchange_wallets(),
        watch_mints()
    )

if __name__ == "__main__":
    asyncio.run(main())
