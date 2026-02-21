import pandas as pd
import numpy as np
from ai.model_loader import AIModel

def load_training_data():
    print("📊 Loading training data...")
    return pd.DataFrame({
        "open": np.random.rand(100),
        "high": np.random.rand(100),
        "low": np.random.rand(100),
        "close": np.random.rand(100),
        "volume": np.random.rand(100)
    })

def train_model():
    print("🚀 Training AI Model...")
    data = load_training_data()
    model = AIModel()
    model.train(data)
    model.save()
    print("✅ Training completed and model saved.")

if __name__ == "__main__":
    train_model()
