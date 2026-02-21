import asyncio

class LifecycleManager:
    def __init__(self):
        self.running = True

    async def initialize(self):
        print("🔧 Initializing bot components...")
        await asyncio.sleep(1)
        print("✅ Initialization complete.")

    async def shutdown(self):
        print("🛑 Shutting down bot...")
        self.running = False
        await asyncio.sleep(1)
        print("✔️ Bot stopped.")
