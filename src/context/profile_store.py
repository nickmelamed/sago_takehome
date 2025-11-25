''' Stores all information for company profile
'''

class ProfileStore:
    """
    Context store combining email history, notes, and metadata.
    """
    def __init__(self, email_data):
        self.founder = email_data["founder"]
        self.company = email_data["company"]
        self.last_email = email_data["last_email"]
        self.notes = email_data["investor_notes"]

    def summary(self):
        return {
            "founder": self.founder,
            "company": self.company,
            "last_email_snippet": self.last_email["snippet"],
            "notes": self.notes
        }
