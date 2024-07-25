# Job Finder, Hackathons & Events, Profile Recommendations, and Vehicle Micro Agents

This repository contains a collection of AI agents developed using Fetch.ai technology, including uAgent, Agentverse, and DeltaV. Each agent is designed to perform specific tasks such as finding job listings, providing details about hackathons and events, recommending professional profiles, and retrieving vehicle details including challan information.

## Table of Contents

- [Job Finder Agent](#job-finder-agent)
- [Hackathons and Events Agent](#hackathons-and-events-agent)
- [Profile Recommendations Agent](#profile-recommendations-agent)
- [Vehicle Micro Agents with Challan Details](#vehicle-micro-agents-with-challan-details)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Job Finder Agent

The Job Finder Agent assists users in finding job listings based on a provided job description. It utilizes the LinkedIn Data API to fetch relevant job details and provide them to the user.

### Features
- Search for jobs using keywords.
- Retrieve job details including title, company, location, and posting date.

## Hackathons and Events Agent

The Hackathons and Events Agent helps users discover upcoming events, hackathons, and meetups based on provided event descriptions and locations.

### Features
- Search for events using keywords and location.
- Retrieve event details including name, date, community, and registration link.

## Profile Recommendations Agent

The Profile Recommendations Agent provides recommendations for professional profiles based on a provided profile description. It uses the LinkedIn Data API to fetch and display profile details.

### Features
- Search for professional profiles using keywords.
- Retrieve profile details including name, title, location, and summary.

## Vehicle Micro Agents with Challan Details

The Vehicle Micro Agents retrieve details about vehicles using their registration numbers. This includes comprehensive information such as owner details, vehicle specifications, and challan details.

### Features
- Fetch vehicle details using registration numbers.
- Retrieve owner information, vehicle specifications, insurance details, and challan information.

## Getting Started

<h3 align="center" style="margin-bottom: 40px; font-weight: lighter">
  <p>Fetch.ai's vision is to create an AI-empowered platform that can connect services and APIs without any domain knowledge. Our technology is built on four key components: AI Agents, the Agentverse, the AI Engine, and the Fetch Network. AI Agents are independent decision-makers that connect to the network and represent data, APIs, services and people, while the Agentverse serves as a development platform for these agents. The AI Engine links human input to AI actions, and the Fetch Network underpins the entire system, ensuring smooth operation and integration.</p>
</h3>

The uAgent Library, the library behind the agents:

- [`uAgents`](https://github.com/fetchai/uAgents) - python library for uagents src.

Build and deploy agents with Agentverse.ai; a hosting and agent management platform.
- [`Agentverse↗️`](https://agentverse.ai) - the platform for building production ready AI agents.

Chat with AI Agents using DeltaV; the gateway to the AI-Engine:
- [`DeltaV↗️`](https://deltav.agentverse.ai) - Enjoy a simple web interface to chat with AI agents as part of DeltaV

Essential reading:
- [`Create an agent↗️`](https://fetch.ai/docs/guides/agents/create-a-uagent) - A simple guide to get you moving quickly 
- [`What is AI Engine↗️`](https://fetch.ai/docs/concepts/ai-engine/ai-engine-intro) - Our AI multi-model system, utilising LLMs. 
- [`What is Fetch.ai↗️`](https://fetch.ai/docs/concepts/introducing-fetchai) - Our tech stack and ecosystem. 

### Prerequisites
- Python 3.8 or higher
- `uagents` library
- `requests` library
- `rapid api` 

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gautammanak1/Fetch.ai-agents.git
   cd Fetch.ai-agents

2. Install the required Python packages:
```
pip install -r requirements.txt
```

3. Running the Agents
To run any of the agents, execute the following command:
```
python <agent_filename>.py
```
### Contributing
We welcome contributions to improve and expand the functionality of these agents. Please fork the repository, create a new branch, and submit a pull request with your changes.
