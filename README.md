# 🌤️ LLM Tool Call Weather Assistant

A conversational weather app: ask about the weather in natural language and get real-time forecasts.

## How It Works

1. **LLM** (`llama-3.1-8b-instant`) extracts city and country from your query
2. **Geopy** converts the location to coordinates
3. **Open-Meteo API** fetches current weather in the city.
4. **LLM** generates a friendly response.

## Features

- Current weather conditions
- Natural language input (e.g. *"What's the weather in Paris in 2 hours?"*)

## Setup

```bash
git clone https://github.com/yourusername/llm-tool-call-weather-assistant
cd llm-tool-call-weather-assistant
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
```

Run the app:
```bash
streamlit run app.py
```

## Tech Stack

| Component | Tool |
|-----------|------|
| LLM & Tool Calling | [Groq](https://groq.com) — `llama-3.1-8b-instant` |
| Geocoding | [Geopy](https://geopy.readthedocs.io) |
| Weather API | [Open-Meteo](https://open-meteo.com) |
| UI | [Streamlit](https://streamlit.io) |

