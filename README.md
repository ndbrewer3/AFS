### Dynamic Freight Routing Agent

## Overview
Built for the APX Frontier Labs Build Challenge, this project is an autonomous agentic logistics dispatcher. It utilizes a ReAct (Reason + Act) loop to dynamically evaluate freight routes, detect live disruptions, and mathematically calculate the most cost-effective alternative paths using simulated network data. 

## System Architecture
* **Orchestration:** LangGraph (ReAct Agent architecture)
* **Tool Server:** FastMCP (Model Context Protocol for exposing local databases/functions to the LLM)
* **LLM Engine:** Google Gemini API (`gemini-3.8-flash`)

## Key Capabilities
1. **Disruption Detection:** The agent proactively queries the FastMCP server to check specific network hubs (e.g., Raleigh, Charlotte) for real-time delays or closures.
2. **Dynamic Rerouting:** If a primary route is blocked, the agent autonomously identifies valid alternative hubs based on strict system constraints.
3. **Cost Optimization:** The agent queries carrier rates (Swift, FedEx, TForce) and mileage data to calculate and recommend the cheapest viable transit path.

## Project Structure
* `mock_data.py`: The simulated logistics network data, including available hubs, mileage, carrier rates, and active route disruptions.
* `client.py`: The main LangGraph agent and ReAct execution loop.
* `server.py`: The FastMCP server hosting the routing tools, mock carrier rates, and disruption databases.
* `demo.py`: A zero-latency simulation script used for presentations in the event of live LLM API timeout errors (e.g., 503/504).
* `requirements.txt`: Project dependencies.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
2. **Install Dependencies:**
   pip install -r requirements.txt
3. **Configure the environment:**
   Create a .env file in the root directory and add your Google Gemini API key:
   GOOGLE_API_KEY="your_api_key_here"

## Execution

1. **Run the the live ReAct Agent:**
   This will spin up the FastMCP server over standard input/output (stdio) and initiate the multi-step LLM reasoning loop.
   ```bash
   python client.py
2. **Run the Demo:**
   If the live API is experiencing latency or quota limits, run the fallback simulation to view the expected output and business logic.
   ```bash
   python demo.py