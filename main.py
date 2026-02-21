import asyncio
from ai.model_loader import AIModel
from core.news_fetcher import NewsFetcher
from core.price_action import PriceActionAnalyzer
from core.decision_engine import DecisionEngine
from core.lifecycle import LifecycleManager

async def main():
    print("🚀 Binary Pro Bot V2 Started")

    model = AIModel()
    news = NewsFetcher()
    pa = PriceActionAnalyzer()
    engine = DecisionEngine()
    lifecycle = LifecycleManager()

    await lifecycle.initialize()

    while True:
        try:
            market_data = await pa.get_market_snapshot()
            news_data = await news.get_latest_news()
            ai_signal = model.predict(market_data, news_data)
            decision = engine.generate_decision(ai_signal, market_data)

            print("📌 Decision:", decision)

            await asyncio.sleep(2)

        except Exception as e:
            print("❌ Error:", e)
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
