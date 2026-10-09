
import streamlit as st
import traceback
import asyncio

# Update this import to match your actual CrewAI workflow file.
from src.main_tasks import get_trip_plan
# Apply the workaround first
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg

# Then import CrewAI and your project modules
import streamlit as st

from src.main_tasks import get_trip_plan

st.set_page_config(
    page_title="AI Multi-Agent Trip Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------- PAGE STYLING --------------------

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #808080;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 48px;
        font-weight: bold;
    }

    .result-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------- HEADER --------------------

st.markdown(
    '<div class="main-title">✈️ AI Multi-Agent Trip Planner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Plan smarter trips with specialized AI agents for research, '
    'transportation, hotels, activities, budgets, and itineraries.'
    '</div>',
    unsafe_allow_html=True
)


# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.header("🤖 AI Travel Assistant")

    st.write(
        "Your AI travel team works together to create "
        "a personalized travel plan."
    )

    st.divider()

    st.subheader("Available Agents")

    st.markdown(
        """
        - 🔎 Travel Research Agent
        - 🚗 Transportation Agent
        - 🏨 Hotel Agent
        - 🎯 Activity Agent
        - 💰 Budget Agent
        - 📅 Itinerary Agent
        """
    )

    st.divider()

    st.caption("Powered by Python, Streamlit and CrewAI")


# -------------------- TRIP INPUT FORM --------------------

st.subheader("🌍 Plan Your Next Trip")

with st.form("trip_planning_form"):

    col1, col2 = st.columns(2)

    with col1:
        source = st.text_input(
            "Starting Location",
            placeholder="e.g., Bangalore"
        )

        destination = st.text_input(
            "Destination",
            placeholder="e.g., Goa"
        )

        days = st.number_input(
            "Number of Days",
            min_value=1,
            max_value=30,
            value=5,
            step=1
        )

    with col2:
        travelers = st.number_input(
            "Number of Travelers",
            min_value=1,
            max_value=50,
            value=2,
            step=1
        )

        budget = st.number_input(
            "Total Budget (₹)",
            min_value=1000,
            max_value=10000000,
            value=40000,
            step=1000
        )

        interests = st.multiselect(
            "Travel Interests",
            options=[
                "Beaches",
                "Adventure",
                "Nature",
                "Historical Places",
                "Culture",
                "Local Food",
                "Shopping",
                "Wildlife",
                "Photography",
                "Nightlife"
            ],
            default=["Beaches", "Local Food"]
        )

    special_requirements = st.text_area(
        "Additional Requirements (Optional)",
        placeholder=(
            "e.g., Prefer budget hotels, avoid long journeys, "
            "include family-friendly activities..."
        )
    )

    submitted = st.form_submit_button(
        "✈️ Plan My Trip",
        type="primary"
    )


# -------------------- GENERATE TRIP PLAN --------------------

if submitted:

    if not source.strip() or not destination.strip():
        st.error("Please enter both the starting location and destination.")

    elif source.strip().lower() == destination.strip().lower():
        st.error("Starting location and destination must be different.")

    elif not interests:
        st.error("Please select at least one travel interest.")

    else:
        trip_inputs = {
            "source": source.strip(),
            "destination": destination.strip(),
            "days": int(days),
            "travelers": int(travelers),
            "budget": int(budget),
            "interests": ", ".join(interests),
            "special_requirements": (
                special_requirements.strip()
                if special_requirements.strip()
                else "No additional requirements"
            )
        }

        st.divider()
        st.subheader("🧳 Your Personalized Travel Plan")

        with st.spinner(
            "AI agents are researching your destination "
            "and preparing your itinerary..."
        ):
            try:
                # Create the CrewAI workflow.
                crew = get_trip_plan(
                            source=trip_inputs["source"],
                            destination=trip_inputs["destination"],
                            days=trip_inputs["days"],
                            travelers=trip_inputs["travelers"],
                            budget=trip_inputs["budget"]
                        )

                # Execute the agents with the user's inputs.
                result = asyncio.run(crew.kickoff_async())

                # CrewAI commonly returns a CrewOutput object.
                # Its raw property contains the final textual result.
                if hasattr(result, "raw"):
                    result_text = result.raw
                else:
                    result_text = str(result)

                if not result_text or not str(result_text).strip():
                    st.warning("The agents returned an empty result.")

                else:
                    st.success("Your trip plan is ready!")

                    # Trip summary
                    st.markdown("### 📍 Trip Summary")

                    metric1, metric2, metric3 = st.columns(3)

                    metric1.metric(
                        "Destination",
                        destination.strip()
                    )

                    metric2.metric(
                        "Duration",
                        f"{int(days)} days"
                    )

                    metric3.metric(
                        "Travelers",
                        int(travelers)
                    )

                    # Final itinerary
                    st.markdown("### 📅 Complete Itinerary")

                    st.markdown(str(result_text))

                    # Allow the user to download the generated plan.
                    st.download_button(
                        label="📥 Download Trip Plan",
                        data=str(result_text),
                        file_name="trip_plan.md",
                        mime="text/markdown"
                    )

            except Exception as exc:
                st.error(
                    "Unable to generate the trip plan. "
                    "Please check your CrewAI configuration "
                    "and try again."
                )

                with st.expander("View error details"):
                    st.code(str(exc))
                    st.code(traceback.format_exc())


# -------------------- FOOTER --------------------

st.divider()

st.caption(
    "Note: AI-generated prices, travel times, and recommendations "
    "are estimates unless verified using live data sources."
)