# Fetch.ai Agents Collection

[![Fetch.ai](https://img.shields.io/badge/Fetch.ai-uAgents-purple)](https://fetch.ai)
[![Agentverse](https://img.shields.io/badge/Agentverse-DeltaV-blue)](https://agentverse.ai)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Integrated-0055DA)](https://rapidapi.com)

A collection of AI agents built with Fetch.ai's uAgents framework, Agentverse, and DeltaV. Each agent performs a specialized task — from job searching and event discovery to profile recommendations and vehicle information retrieval.

## Agents

### 1. Job Finder Agent

Searches for job listings based on a description using the LinkedIn Data API.

- **Input:** Job description (e.g., "remote data scientist")
- **Output:** Matching jobs with title, company, location, and posting date
- **API:** LinkedIn Data API via RapidAPI

### 2. Hackathons & Events Agent

Discovers upcoming tech events, hackathons, and meetups by keyword and location.

- **Input:** Event description + optional location
- **Output:** Event name, date, community, and registration link
- **Data Source:** Static event dataset (extensible to API)

### 3. Profile Recommendations Agent

Finds professional profiles matching a given description using LinkedIn search.

- **Input:** Profile description (e.g., "machine learning engineer India")
- **Output:** Matching profiles with name, title, location, and summary
- **API:** LinkedIn Data API via RapidAPI

### 4. Vehicle Details Agent

Retrieves vehicle registration information and challan (traffic violation) details for Indian vehicles.

- **Input:** Vehicle registration number
- **Output:** Vehicle owner info, registration details, pending challans
- **API:** RTO Vehicle Information API via RapidAPI

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | Fetch.ai uAgents |
| AI Engine | Fetch.ai AI Engine / DeltaV |
| Job Data | LinkedIn Data API (RapidAPI) |
| Vehicle Data | RTO Vehicle Info API (RapidAPI) |
| Data Models | Pydantic |

## Project Structure

```
├── Hackathon and Technical Events agents.py   # Event discovery agent
├── JobAgents.py                                # Job search agent
├── Profile Recommendations Agents.py           # Profile recommendation agent
├── Vehicle micro.py                            # Vehicle details agent
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- RapidAPI key (for LinkedIn Data API and RTO Vehicle API)
- Fetch.ai Agentverse account (for DeltaV deployment)

### Installation

```bash
git clone https://github.com/gautammanak1/Fetch.ai-agents.git
cd Fetch.ai-agents
pip install uagents ai-engine pydantic requests
```

### Configuration

Replace the `rapidapi_key` variable in each agent file with your RapidAPI key:

```python
rapidapi_key = "your_rapidapi_key_here"
```

### Running an Agent

```bash
python JobAgents.py
```

### Deploy to Agentverse

Each agent can be deployed to [Agentverse](https://agentverse.ai) and accessed through DeltaV for natural language interaction.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-agent`)
3. Commit your changes
4. Push and open a Pull Request

## License

MIT
