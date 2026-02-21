class DecisionEngine:
    def __init__(self):
        pass

    def generate_decision(self, ai_signal, market_data):
        decision = {
            "signal": ai_signal,
            "price": market_data["close"],
            "confidence": 0.75 if ai_signal == "BUY" else 0.60
        }
        return decision
