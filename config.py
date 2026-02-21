# ============================
#   Binary Pro Bot V2 Config
# ============================

# 🔐 مفاتيحك الخاصة (ضعها بنفسك)
API_KEY = "8106899856:AAER5PYfDH31Gm-8jc67nYihTdcRd_iA1to "
USER_ID = "5066447725 "
SECRET_KEY = "d6cgk89r01qsiik26590d6cgk89r01qsiik2659g "

# 📁 مسار النموذج
MODEL_PATH = "ai/model.bin"

# 📰 مصادر الأخبار
NEWS_SOURCES = [
    "https://newsapi.org/v2/top-headlines?category=business",
    "https://newsapi.org/v2/top-headlines?category=technology"
]

# 💹 رموز السوق التي يتابعها البوت
MARKET_SYMBOLS = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "BTCUSD",
    "ETHUSD"
]

# 📊 مسار بيانات التدريب
TRAINING_DATA_PATH = "database/training_data.csv"
