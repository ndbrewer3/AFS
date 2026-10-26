# client.py
import asyncio
import os
import warnings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

# Suppress all messy LangChain and Google SDK warnings for a clean demo terminal
warnings.filterwarnings("ignore")

load_dotenv(override=True)

async def run_logistics_desk():
    print("1. Starting system and connecting to MCP Server...")
    
    server_params = StdioServerParameters(command="python", args=["-u", "server.py"])
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            mcp_tools = await load_mcp_tools(session)
            print(f"2. Connected! Successfully loaded {len(mcp_tools)} tools.")
            
            # Upgraded back to the primary model now that your quota has reset
            llm = ChatGoogleGenerativeAI(
                model="gemini-3.8-flash", 
                api_key=os.getenv("GOOGLE_API_KEY"),
                temperature=0,
                max_retries=0,
                timeout=30.0
            )
            
            system_prompt = (
                "You are an expert Logistics Dispatcher and Routing Engineer. "
                "Our ONLY available network hubs are: Washington, D.C., Raleigh, Roanoke, and Charlotte. "
                "You have access to tools that check carrier rates, route disruptions, and transit times. "
                "Always check for disruptions first. If a route is blocked, calculate an alternative using ONLY our available hubs. "
                "Present your final answer as a clean, professional markdown report. "
                "CRITICAL: You must only call ONE tool at a time. Do not make parallel tool calls."
            )
            
            agent = create_react_agent(llm, mcp_tools)
            
            user_input = (
                "We need to route freight from Washington, D.C. to Charlotte. "
                "Check for disruptions in Raleigh. If it is blocked, find the cheapest alternative route."
            )
            print(f"\n3. Executing Prompt: '{user_input}'\n")
            print("Thinking... (this takes a few seconds as the AI uses the tools)...\n")
            
            # Execute the agent cleanly for the presentation
            result = await agent.ainvoke({
                "messages": [
                    ("system", system_prompt),
                    ("human", user_input)
                ]
            })
            
            print("================ FINAL REPORT ================\n")
            print(result["messages"][-1].content)
            print("\n==============================================")

if __name__ == "__main__":
    asyncio.run(run_logistics_desk())