import os
from redis import Redis
import json

def setup_config():
    r = Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    
    # 1. High-Quality Search Keywords
    keywords = [
        "{coin} breaking news",
        "{coin} bullish news",
        "{coin} bearish news",
        "{coin} price surge",
        "{coin} price crash",
        "{coin} liquidation news",
        "{coin} short squeeze",
        "{coin} long squeeze",
        "{coin} whale transfer",
        "{coin} whale alert",
        "{coin} exchange inflow",
        "{coin} exchange outflow",
        "{coin} binance listing",
        "{coin} delisting news",
        "{coin} technical breakout",
        "{coin} resistance breakout",
        "{coin} support breakdown",
        "{coin} volume spike",
        "{coin} open interest surge",
        "{coin} funding rate change",
        "{coin} twitter sentiment",
        "{coin} trending on X",
        "{coin} reddit discussion",
        "{coin} community hype",
        "{coin} influencer opinion",
        "{coin} partnership announcement",
        "{coin} ETF approval",
        "{coin} regulation news",
        "{coin} SEC news",
        "{coin} hack exploit",
        "{coin} security breach",
        "{coin} market sentiment",
        "{coin} trading volume surge"
    ]
    r.delete("news:config:keywords")
    r.sadd("news:config:keywords", *keywords)
    print(f"✅ Loaded {len(keywords)} high-quality keywords into Redis.")

    # 2. News Portals / Sources
    portals = ["google", "duckduckgo", "binance_feed", "crypto_panic", "coindesk", "cointelegraph"]
    r.delete("news:config:portals")
    r.sadd("news:config:portals", *portals)
    print(f"✅ Configured {len(portals)} search portals in Redis.")

    # 2b. AI Engines (Modular) - Including Jina now
    ai_engines = ["gemini", "openai", "claude", "jina"]
    r.delete("news:config:ai_engines")
    r.sadd("news:config:ai_engines", *ai_engines)
    print(f"✅ Configured {len(ai_engines)} AI engines in Redis.")

    # 3. AI Thresholds & Weights
    config = {
        "min_buy_votes": 2,
        "concurrency_limit": 5,
        "min_sentiment_score": 0.15,
        "max_articles_per_coin": 5,
        "ai_boost_weight": 0.2,
        "gemini_api_key": os.environ.get("GEMINI_API_KEY", ""),
        "openai_api_key": os.environ.get("OPENAI_API_KEY", ""),
        "anthropic_api_key": os.environ.get("ANTHROPIC_API_KEY", ""),
        "jina_api_key": os.environ.get("JINA_API_KEY", ""),
        "enable_ai_search": True,
        "enable_portal_search": True,
        "enable_normal_web_search": True
    }
    r.set("news:config:global", json.dumps(config))
    print(f"✅ Set global AI thresholds and weights.")

    print("\n--- Current Redis Config Summary ---")
    print(f"AI Engines: {r.smembers('news:config:ai_engines')}")
    print(f"Keywords: {len(r.smembers('news:config:keywords'))} loaded.")

if __name__ == "__main__":
    setup_config()
