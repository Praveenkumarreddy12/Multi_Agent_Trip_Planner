from crewai import Agent

def get_travel_agent(llm):

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
        llm = llm,
        verbose = True
    )


# def get_transport_agent(llm):

#     return Agent(
        
#     )


def get_hotel_agent(llm):

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


def get_activity_agent(llm):

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

def get_budget_agent(llm):

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


def get_itinerary_agent(llm):

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