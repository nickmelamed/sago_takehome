''' Ingests Signals to be used as inputs for outreach generation
'''

import json

class SignalIngestor:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_signals(self):
        with open(self.filepath, "r") as f:
            return json.load(f)
