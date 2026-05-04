import re


def create_weather_prompt(user_query, weather_data):
    if not weather_data:
        return "No weather data available!"

    prompt = (
        "You are a helpful assistant. Based on the weather data below, answer the user's question in a clear"
        "and simple way. \n\n "
        f"User question: {user_query} \n\n"
        f"Weather data: {weather_data} \n\n"
        "Clearly state the city and the country that you are asked to answer in the format: 'Weather for 'city', 'country'."
        "If the city is missing, the weather will be provided for the capital of the country. "
        "If you cannot access weather data or there could be a typo or issues with user's question, "
        "then just simply ask them to provide further information. Please do not explain any bug!"
        "Summarize the weather information so that it is easy for everyone to understand. Use calm and friendly tone. "
    )

    return prompt


def send_prompt_to_llm(client, prompt):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()
