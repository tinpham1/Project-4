# 🚀 Project 4: Forecasting the Future of Space & Building a Rocket Knowledge Assistant

## 👩‍💻 About the Project

This capstone project explores two complementary applications of data science in the context of space exploration:

1. **Time Series Forecasting**: Using Facebook Prophet, we predicted future NASA space missions through the year 2050 based on historical launch trends.
2. **Rocket Knowledge Assistant**: An AI-powered chatbot that answers natural-language questions about rockets and space missions by combining SQL database queries with OpenAI’s GPT model.

Together, these components showcase how machine learning and AI can make complex data more accessible, predictive, and engaging.

---

## 📈 Forecasting Future Space Missions

We analyzed historical launch data (1957–2022) and used the Prophet model to forecast mission trends through 2050.

### 🔧 Tools Used
- Python (Pandas, Prophet, Matplotlib)
- Tableau (for final visualization)

### ✅ Model Results
- **MAE**: ~11–15 missions/year
- **RMSE**: 13–20
- **MAPE**: 22–28%
- **R² Score**: 0.836

### 📊 Visualizations (Tableau Dashboards)

All visualizations are hosted in Tableau. Use the links below to explore:

1. **[Launch Activity by Year](https://public.tableau.com/authoring/SpaceMissionVisualizations/LaunchActivity#1)**  
   Displays global mission counts by year, segmented by success, failure, partial failure, and pre-launch failure.  
   🔹 *Key Insight*: Spikes in the late 1960s–70s and again in the 2020s reflect key eras of activity.

2. **[Company Launch Performances](https://public.tableau.com/authoring/SpaceMissionVisualizations/CompanyLaunchPerformances#1)**  
   Horizontal bar chart showing missions per agency/company, color-coded by outcome.  
   🔹 *Key Insight*: Russia/USSR has the highest total launch count.

3. **[Rocket Reliability Metrics](https://public.tableau.com/authoring/SpaceMissionVisualizations/RocketReliability#1)**  
   Compares mission frequency of active vs. retired rockets.  
   🔹 *Key Insight*: Cosmos-3M had the most missions historically; Falcon 9 leads among active rockets.

4. **[Mission Forecast (2050)](https://public.tableau.com/authoring/SpaceMissionVisualizations/MissionForecasted#1)**  
   Time series projection using Prophet, with predicted intervals through 2050.  
   🔹 *Key Insight*: The model forecasts ~394 missions in 2050 (range: 316–470).

5. **[Combined Dashboard Overview](https://public.tableau.com/views/SpaceMissionVisualizations/SpaceMissionVisualizations?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**  
   Integrates all visualizations into one interactive dashboard for easy navigation.

---

## 🤖 Rocket Knowledge Assistant

The Rocket Knowledge Assistant is a chatbot that answers questions about space missions, rockets, and launches. It intelligently routes queries to a database or to OpenAI’s GPT API depending on question complexity.

### 🔧 Tools Used
- Python (Flask)
- SQLite (Mission Database)
- OpenAI API
- Optional: LangChain (for orchestration)

### 💬 How It Works
1. User asks a question (e.g., “Which rocket launched the most missions?”)
2. The system detects intent and chooses between a SQL lookup or AI-generated response
3. The chatbot responds with a clear, conversational answer

### 🌍 Why It Matters
- Makes space knowledge accessible to everyone
- Great for students, space enthusiasts, and general users
- Demonstrates how AI + structured data can work together

---

## 👥 Team

- Tin
- Avenika  
- Melissa  
- Anthony


