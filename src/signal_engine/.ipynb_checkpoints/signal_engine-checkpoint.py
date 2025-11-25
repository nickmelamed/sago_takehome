''' 
'''

import datetime

class SignalEngine:
    WEIGHTS = { # can customize weights depending on how much you believe each category matters, or add more categories 
        "funding_round": 0.9,
        "hiring": 0.7,
        "product_launch": 0.85
    }

    def score_signal(self, signal):
        base = self.WEIGHTS.get(signal["type"], 0.3)

        # Freshness boost (how recent is a given signal?) 
        days_ago = (datetime.datetime.now().date() - 
                    datetime.datetime.fromisoformat(signal["date"]).date()).days
        
        freshness = max(0.1, 1 - min(days_ago / 120, 1))

        return round(base * freshness, 2)
