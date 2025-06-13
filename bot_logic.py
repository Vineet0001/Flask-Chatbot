import time
import re
import requests
import wikipedia
import openai
from config import OPENWEATHER_API_KEY, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
user_name = ""

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"It's {temp}°C in {city} with {desc}."
        else:
            return "Could not fetch weather data."
    except:
        return "Error fetching weather."

def get_time():
    return time.ctime()

def is_math_expression(text):
    return bool(re.fullmatch(r"[0-9+\-*/(). ]+", text))

def evaluate_math_expression(expr):
    try:
        result = eval(expr)
        return f"The answer is: {result}"
    except:
        return "Invalid math expression."

def get_wikipedia_summary(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return "Sorry, I couldn't find that on Wikipedia."

def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except:
        return "GPT couldn't process that cause of you are out of token."

def get_bot_response(user_input):
    global user_name
    user_input_lower = user_input.lower()

    if user_input_lower in ["hi", "hello", "hey", "hi chatbot", "hello bot", "hey bot", "hi there", "hello there", "Namaste", "Bonjour", "Hola"]:
        return "Namaste! How can I help you today?"

    if "my name is" in user_input_lower:
        user_name = user_input.split("is")[-1].strip().capitalize()
        return f"Nice to meet you, {user_name}!"

    if "what is my name" in user_input_lower:
        return f"You are {user_name}!" if user_name else "I don't know your name yet. Tell me!"

    if "time" in user_input_lower:
        return get_time()

    if "weather" in user_input_lower:
        city = user_input_lower.split("in")[-1].strip() if "in" in user_input_lower else "your city"
        return get_weather(city)

    if is_math_expression(user_input):
        return evaluate_math_expression(user_input)

    if "bye" in user_input_lower:
        return "Goodbye! Stay safe!"

    wiki_summary = get_wikipedia_summary(user_input)
    if wiki_summary:
        return wiki_summary

    return get_gpt_response(user_input)
