import os
import re

from dotenv import load_dotenv
from groq import Groq

from utils import *


def perform_rag(client, user_query):

    # extract location name:
    location_name = extract_the_city_and_country(client, user_query)

    # extract geo_coords:
    geo_coords = get_coordinates_for_city(location_name)

    # get weather data
    weather_data = get_current_weather_open_meteo(*geo_coords)

    # format prompt:
    format_prompt = create_weather_prompt(user_query, weather_data)

    # get final answer:
    final_answer = send_prompt_to_llm(client, format_prompt)

    return final_answer


# if __name__ == "__main__":
#     user_query = "What is the weather like in Melbourne?"
#     load_dotenv()
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#     final_answer = perform_rag(client, user_query)
#     sentences = re.split(r'(?<=[.!?])\s+', final_answer)

#     for sentence in sentences:
#         print(sentence)
