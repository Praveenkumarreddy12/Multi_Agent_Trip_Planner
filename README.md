# Multi_Agent_Trip_Planner
A Multi-Agent AI Trip Planner built with Python and CrewAI to generate personalized travel itineraries, recommend activities and accommodations, and estimate trip budgets using specialized AI agents.


# ✈️ Multi-Agent Trip Planner

## 📌 Project Overview

The **Multi-Agent Trip Planner** is an AI-powered travel planning application built with Python and CrewAI. It uses multiple specialized AI agents to help users plan personalized trips based on their destination, travel duration, budget, number of travelers, and personal interests.

Each agent handles a specific task, such as travel research, transportation planning, accommodation recommendations, activity selection, budget estimation, and itinerary generation. The agents work together to generate a structured travel plan.

## 🎯 Key Features

* **Travel Research:** Explore destinations and discover popular attractions.
* **Transportation Planning:** Compare travel options and estimate transportation costs.
* **Accommodation Recommendations:** Identify suitable places to stay based on the user's budget.
* **Activity Recommendations:** Suggest attractions, activities, and local experiences.
* **Budget Estimation:** Estimate expenses for transportation, accommodation, food, and activities.
* **Daily Itinerary Generation:** Create organized, day-by-day travel plans.
* **Personalized Planning:** Customize recommendations based on user preferences and trip requirements.

## 🤖 AI Agents

| Agent                 | Responsibility                                       |
| --------------------- | ---------------------------------------------------- |
| Travel Research Agent | Researches the destination and tourist attractions.  |
| Transportation Agent  | Suggests transportation options and estimates costs. |
| Hotel Agent           | Recommends suitable accommodation.                   |
| Activity Agent        | Suggests activities and places to visit.             |
| Budget Agent          | Estimates expenses and checks the overall budget.    |
| Itinerary Agent       | Combines recommendations into a daily travel plan.   |

## 🛠️ Technology Stack

* **Programming Language:** Python
* **Multi-Agent Framework:** CrewAI
* **LLM Integration:** Groq or Ollama
* **Backend API:** FastAPI
* **Frontend:** Streamlit
* **Data Validation:** Pydantic
* **Environment Configuration:** Python-dotenv
* **Version Control:** Git and GitHub

*The technology list represents the planned stack; update it to reflect the components implemented in the current version.*

## 🏗️ Project Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  v
Trip Orchestrator
  |
  +--> Travel Research Agent
  |
  +--> Transportation Agent
  |
  +--> Hotel Agent
  |
  +--> Activity Agent
  |
  +--> Budget Agent
  |
  +--> Itinerary Agent
  |
  v
Personalized Travel Plan
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi_agent_trip_planner.git
cd multi_agent_trip_planner
```

Replace `YOUR_USERNAME` with your GitHub username and use your actual repository name.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

For Groq:

```env
GROQ_API_KEY=your_groq_api_key
```

For Ollama, configure the model and local endpoint according to your implementation. A cloud API key is not required when using a compatible local Ollama model.

**Security:** Never upload API keys or your `.env` file to GitHub.

### 5. Run the Application

Run the commands supported by your implementation.

For a Streamlit frontend:

```bash
streamlit run frontend/streamlit_app.py
```

For a FastAPI backend:

```bash
uvicorn app.main:app --reload
```

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## 🧪 Example Use Case

**User Input**

```text
Source: Bangalore
Destination: Goa
Duration: 5 days
Travelers: 2
Budget: ₹40,000
Interests: Beaches, adventure, and local food
```

**Expected Output**

* Destination research and attraction recommendations
* Transportation options and estimated costs
* Accommodation suggestions
* A day-by-day travel itinerary
* An estimated expense breakdown
* Suggestions to adjust the plan if the budget is exceeded

*Example outputs are illustrative. Actual prices and availability must be verified with current travel providers.*

## 🚀 Future Enhancements

* Real-time weather integration
* Web search for destination research
* Maps and location-based recommendations
* Live flight, train, and hotel availability integrations
* PostgreSQL database for saving trip plans
* Retrieval-Augmented Generation (RAG) for travel documents
* Budget optimization and automatic itinerary revision
* Docker-based deployment
* Automated testing and CI/CD

## 🎓 Learning Outcomes

This project demonstrates practical applications of:

* Multi-agent system design and orchestration
* Large Language Model (LLM) integration
* Prompt engineering and task decomposition
* Python backend development
* REST API development with FastAPI
* Frontend development with Streamlit
* Environment management and API security
* Software testing and version control

## 👨‍💻 Author

**Praveen Kumar Reddy**

GitHub: [Praveenkumarreddy12](https://github.com/Praveenkumarreddy12)

---

⭐ If you find this project useful, consider giving the repository a star.
