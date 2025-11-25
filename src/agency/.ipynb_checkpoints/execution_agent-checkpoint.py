''' Execution of Slack aproval and Gmail send
'''

import json
import os

class ExecutionAgent:
    """
    Simulates Slack approval and Gmail send.
    """

    def approve_and_send(self, email_text, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump({"sent_email": email_text}, f, indent=2)