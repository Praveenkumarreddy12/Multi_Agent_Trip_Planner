import os
import asyncio
import time

from dotenv import load_dotenv
from crewai import Task, Crew, Process, LLM
from src.main_agents import (
    get_activity_agent,
    get_budget_agent,
    get_hotel_agent,
    get_itinerary_agent,
    get_travel_agent,
    get_transport_agent
)

load_dotenv()



def get_sleep(output):
    time.sleep(100)

def get_trip_plan( source : str, destination : str, days : int , travelers : int, budget : int) :
    
    research_task = Task(
        description=f"""
        Research from {source} to {destination} for a {days}-day trip.

        Identify:
        - Important tourist attractions
        - Best areas to visit
        - Local experiences
        - Travel considerations
        """,

        expected_output="""
        -Not reach above 500 tokens
        -give me the main points and remove unnecessary points, words, sentences etc..
        -A structured travel research report. 

        """,

        agent=get_travel_agent(),
        callback= get_sleep
    )

    transport_task = Task(
        description="""
        Plan transportation for a trip from {source} to
        {destination} lasting {days} days for {travelers} travelers.

        Identify:
        - Available transportation options such as flights,
        trains, buses, or driving
        - Estimated one-way and round-trip costs
        - Approximate travel duration
        - Local transportation options at the destination
        - Estimated local transportation expenses
        - The most suitable option based on the budget of {budget}

        Compare the available options and recommend a practical
        transportation plan.

        Do not claim live availability or exact prices unless
        verified through a reliable data source.
        """,

        expected_output="""
        -Not reach above 400 tokens
        -give me the main points and remove unnecessary points, words, sentences etc..
        A structured transportation report containing:
        - Available transportation options
        - Estimated travel time for each option
        - Estimated round-trip cost for all travelers
        - Recommended transportation option
        - Local transportation recommendations
        - Estimated local travel expenses
        - Total estimated transportation budget.
        """,

        agent=get_transport_agent(),
        context= [research_task],
        callback= get_sleep
    )

    hotel_task = Task(
    description=f"""
    Recommend suitable accommodation in {destination}
    for {travelers} travelers staying for {days} days.

    Consider the total trip budget of {budget} and the
    user's travel preferences.

    Identify:
    - Suitable hotels, hostels, resorts, or guesthouses
    - Recommended areas to stay
    - Estimated accommodation cost per night
    - Total estimated accommodation cost
    - Proximity to tourist attractions and transportation
    - Amenities, comfort, and suitability
    - Budget-friendly alternatives

    Prioritize accommodation that provides good value
    and fits the overall travel budget.

    Clearly distinguish verified accommodation details
    from estimates or illustrative recommendations.
    """,

    expected_output="""
    -Not reach above 300 tokens
    -give me the main points and remove unnecessary points, words, sentences etc..
    A structured accommodation report containing:
    - Recommended accommodation options
    - Location and key amenities
    - Estimated price per night
    - Estimated total stay cost
    - Advantages of each option
    - Best accommodation recommendation
    - Budget-friendly alternatives.
    .
    """,

    agent=get_hotel_agent(),
    context=[research_task, transport_task],
    callback= get_sleep
    )

    activity_task = Task(
    description=f"""
    Recommend activities and experiences for a {days}-day
    trip to {destination}.

    Consider the user's interests, travel budget of {budget},
    and the research provided by the Travel Research Agent.

    Identify:
    - Popular attractions and sightseeing locations
    - Adventure activities and outdoor experiences
    - Cultural and historical attractions
    - Local food and dining experiences
    - Free and low-cost activities
    - Estimated entry fees and activity costs
    - Suggested activities for each day
    - Approximate time required for each activity

    Avoid scheduling too many activities on a single day.
    Group nearby attractions together to reduce travel time.
    """,

    expected_output="""
    -Not reach above 400 tokens
    -give me the main points and remove unnecessary points, words, sentences etc..
    A structured activity recommendation report containing:
    - Recommended attractions and experiences
    - Activities grouped by day
    - Estimated cost per activity
    - Approximate duration of each activity
    - Local food recommendations
    - Free and budget-friendly alternatives
    - Estimated total activity expenses.
    .
    """,

    agent=get_activity_agent(),
    context= [hotel_task],
    callback= get_sleep
    )

    budget_task = Task(
    description=f"""
    Calculate and analyze the estimated budget for a trip
    from {source} to {destination} for {days} days
    with {travelers} travelers.

    The total budget provided by the user is {budget}.

    Use the transportation, accommodation, and activity
    recommendations from the previous agents.

    Calculate:
    - Round-trip transportation expenses
    - Local transportation expenses
    - Accommodation expenses
    - Food and dining expenses
    - Activity and attraction expenses
    - Miscellaneous expenses
    - Emergency contingency allowance
    - Total estimated trip cost
    - Remaining budget or budget deficit

    Check that the calculations are consistent and avoid
    double-counting expenses.

    If the estimated cost exceeds the user's budget,
    recommend practical cost-saving adjustments.

    Do not invent exact prices. Clearly identify estimates
    and state any assumptions used in calculations.
    """,

    expected_output="""
    -Not reach above 500 tokens
    -give me the main points and remove unnecessary points, words, sentences etc..
    A detailed budget analysis containing:
    - Expense breakdown by category
    - Estimated transportation costs
    - Estimated accommodation costs
    - Estimated food costs
    - Estimated activity costs
    - Miscellaneous and contingency costs
    - Total estimated trip cost
    - User's available budget
    - Remaining balance or budget deficit
    - Budget status: within budget or over budget
    - Cost-saving recommendations when required.
    
    """,

    agent=get_budget_agent(),
    context=[transport_task,hotel_task,activity_task],
    callback= get_sleep
    )

    itinerary_task = Task(
    description=f"""
    Create a complete day-by-day travel itinerary for
    {source} to {destination} for {days} days with
    {travelers} travelers.

    The user's total budget is {budget}.

    Use the research, transportation, accommodation,
    activity, and budget reports generated by the
    previous agents.

    Create an itinerary that includes:
    - Travel and arrival arrangements
    - Daily morning, afternoon, and evening activities
    - Tourist attractions and local experiences
    - Recommended food and dining stops
    - Approximate activity durations
    - Transportation between locations
    - Accommodation arrangements
    - Estimated daily expenses
    - Total estimated trip cost

    Organize activities geographically to reduce
    unnecessary travel.

    Ensure the plan is realistic for the trip duration.
    Follow the Budget Agent's recommendations if the
    estimated expenses exceed the user's budget.

    Do not present unverified prices or availability
    as confirmed facts.
    """,

    expected_output="""
    -Not reach above 800 tokens
    -give me the main points and remove unnecessary points, words, sentences etc..
    A complete, well-organized travel itinerary containing:

    1. Trip summary
       - Source and destination
       - Duration and number of travelers
       - Total estimated budget

    2. Day-by-day itinerary
       - Morning activities
       - Afternoon activities
       - Evening activities
       - Transportation suggestions
       - Food and dining recommendations
       - Estimated daily expenses

    3. Accommodation recommendations

    4. Transportation summary

    5. Complete expense breakdown

    6. Total estimated trip cost and remaining budget

    7. Practical travel tips and important considerations

    The final itinerary must be clear, realistic,
    budget-conscious, and easy for the user to follow.
    and not reach above 5000 tokens
    """,

    agent=get_itinerary_agent(),
    context=[transport_task,hotel_task,activity_task, budget_task],
    callback= get_sleep
    )

    crew = Crew(
            agents=[get_travel_agent(), get_transport_agent(), get_hotel_agent(), get_activity_agent(), get_budget_agent(), get_itinerary_agent()],
            tasks= [research_task, transport_task, hotel_task, activity_task,budget_task, itinerary_task],
            process= Process.sequential,
            verbose= True
        )

    return crew