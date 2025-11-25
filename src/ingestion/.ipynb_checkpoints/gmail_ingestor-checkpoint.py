''' Ingests Gmails to be used as inputs for outreach generation
'''

import json

class GmailIngestor:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        with open(self.filepath, "r") as f:
            data = json.load(f)
        return data