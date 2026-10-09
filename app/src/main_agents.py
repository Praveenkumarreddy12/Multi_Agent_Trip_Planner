import os

from crewai import Agent, LLM
from crewai_tools import SerperDevTool, FileReadTool
from src.tools import get_weather

search_tool = SerperDevTool(max_usage_count=1)
file_tool = FileReadTool()



llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key = os.getenv("GROQ_API_KEY"),
    temperature = 0.3
)

def get_travel_agent():

    return Agent(
        role="Travel Research Specialist",

        goal=(
            "Research the destination and provide useful "
            "travel information for the user's trip."
        ),

        backstory=(
            "You are an experienced travel researcher who "
            "understands destinations, tourist attractions, "
            "travel seasons and local experiences."
        ),
        tools = [search_tool,file_tool,get_weather],
        llm = llm,
        verbose = True
    )


def get_transport_agent():

    return Agent(
        role = "Transport and Travel Logistics Specialist",

        goal = "Find and recommend the most suitable transportation options for the trip, including flights,"
        " trains, buses, and rental cars. Compare available options based on cost, travel duration, convenience, "
        "and traveler preferences. Provide a clear transportation plan that fits the user's budget and itinerary.",

        backstory = "You are an experienced transport and travel logistics specialist with extensive knowledge of transportation planning"
        " and route optimization. You help travelers choose the best ways to reach their destinations by comparing different modes"
        " of transport, estimated travel costs, journey durations, and convenience. You coordinate with the trip planner"
        " agent to ensure that transportation arrangements match the travel itinerary and budget. Your goal is to make"
        " every journey affordable, comfortable, efficient, and well-organized. You distinguish verified information"
        " from estimates and never claim that a ticket is available or booked without confirmation.",
        llm = llm,
        verbose = True
    )


def get_hotel_agent():

    return Agent(
         role="Hotel Specialist",

        goal=(
            "Find suitable accommodation options based on "
            "destination, budget, duration and traveler preferences."
        ),

        backstory=(
            "You are a hotel and accommodation specialist "
            "who compares locations, prices and suitability."
        ),

        llm=llm,

        verbose=True
    )


def get_activity_agent():

    return Agent(
        role="Travel Activity Specialist",

        goal=(
            "Recommend attractions, activities, restaurants "
            "and experiences that match the user's preferences."
        ),

        backstory=(
            "You are an experienced travel planner who knows "
            "how to create enjoyable destination experiences."
        ),

        llm=llm,

        verbose=True
    )

def get_budget_agent():

    return Agent(
        role="Travel Budget Analyst",

        goal=(
            "Calculate the estimated trip cost and ensure "
            "the itinerary stays within the user's budget."
        ),

        backstory=(
            "You are a financial travel planner who carefully "
            "calculates transportation, accommodation, food "
            "and activity costs."
        ),

        llm=llm,

        verbose=True
    )


def get_itinerary_agent():

    return Agent(
        role="Professional Itinerary Planner",

        goal=(
            "Create a practical day-by-day travel itinerary "
            "using the research provided by the other agents."
        ),

        backstory=(
            "You are an expert itinerary designer who creates "
            "realistic and enjoyable travel plans."
        ),

        llm=llm,

        verbose=True
    )