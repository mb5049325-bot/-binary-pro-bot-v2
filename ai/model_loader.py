import pickle
import numpy as np

class AIModel:
    def __init__(self):
        self.model = None
        self.model_path = "ai/model.bin"

    def predict(self, market_data, news_data):
        if self.model is None:
            self.load()

        # نموذج بسيط للتجربة
        value = np.random.rand()
        if value > 0.5:
            return "BUY"
        else:
            return "SELL"

    def train(self, data):
        # تدريب وهمي
        self.model = {"trained": True}

    def save(self):
        with open(self.model_path, "wb") as f:
            pickle.dump(self.model, f)

    def load(self):
        try:
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
        except:
            self.model = {"trained": False}
