# Investor Follow-Up Workflow
This repository contains a lightweight prototype demonstrating how Sago can 
detect meaningful startup progression signals, determine when an investor 
should re-engage with a founder, and generate personalized outreach.

This prototype focuses on:
- Gmail ingestion (mocked via JSON)
- Founder/company profile store
- A simple signal scoring engine
- Personalized outreach generation
- Execution layer stub (e.g., Slack approval → Gmail send)

## Repo Tree

```
sago-reengagement-prototype/
│
├── README.md
├── architecture/
│   └── architecture.pdf
│
├── src/
│   ├── ingestion/
│   │   ├── gmail_ingestor.py
│   │   └── signal_ingestor.py
│   ├── context/
│   │   └── profile_store.py
│   ├── signal_engine/
│   │   └── signal_engine.py
│   ├── outreach/
│   │   └── outreach_generator.py
│   ├── agency/
│   │   └── execution_agent.py
│   └── main.py
│
├── sample_data/
│   ├── emails.json
│   ├── signals.json
│   └── sample_output.json
│
└── requirements.txt
```

## Architecture Overview
See `/architecture/architecture.pdf`.

High-level components:
1. **Data Ingestion** – imports Gmail threads and event signals.
2. **Context Store** – maintains founder/investor relationship data.
3. **Signal Engine** – scores events and determines when to re-engage.
4. **Outreach Generator** – creates a personalized outreach.
5. **Execution Agent** – simulates Slack approval + Gmail send.

This prototype uses mocked data only.

---

## Running the Prototype

### 1. Install dependencies

`pip install requirements.txt`

### 2. Run the main pipeline 

`python src/main.py`

This will:
- load sample emails and signals
- evaluate the signal scoring engine
- generate a personalized outreach draft
- save the output to `/sample_data/sample_output.json`


### Sample Inputs
Located in `/sample_data`:

- `emails.json` — last email + notes between investor + founder  
- `signals.json` — set of mock startup progression events  

---

### Sample Output
The file `sample_output.json` includes:
- triggering signal
- signal score
- generated outreach email

## Notes
This is not a production system.
It is designed to reflect Sago’s key principles:
- **seamless integration** (Gmail, Slack stubs),
- **hyper-personalization** (context-aware generation),
- **true agency** (automated outreach execution flow).




