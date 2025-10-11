from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
import os

from src.tools.search_tool import search_stellar_cartography
from src.tools.calculator_tool import engineering_calculations
from src.tools.mission_logs_tool import (create_mission_log, list_mission_logs, read_mission_log)
from src.prompts.system_prompt import STARFLEET_SYSTEM_PROMPT

load_dotenv()

def create_starfleet_agent():
    """Create a Starfleet-themed agent using the ReAct framework."""

    # Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # Tools available to the agent
    tools = [
    search_stellar_cartography,
    engineering_calculations,
    create_mission_log,      
    list_mission_logs,
    read_mission_log,
]

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=SystemMessage(content=STARFLEET_SYSTEM_PROMPT)
    )

    return agent

# Create the agent instance
starfleet_agent = create_starfleet_agent()