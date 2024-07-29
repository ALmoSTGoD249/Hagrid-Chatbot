import os
import pyautogui
import openai
import webbrowser
import requests
import json
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import datetime
import time

console = Console()

def get_user_input():
    return Prompt.ask("At your command").lower()

def execute_command(command):
    if 'open notepad' in command:
        os.system('notepad.exe')
        console.print("Opening Notepad...", style="bold green")
    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        console.print(f"Searching for {search_query}...", style="bold green")
    elif 'shutdown' in command:
        os.system('shutdown /s /t 1')
        console.print("Shutting down...", style="bold red")
    elif 'restart' in command:
        os.system('shutdown /r /t 1')
        console.print("Restarting...", style="bold yellow")
    elif 'change volume' in command:
        if 'up' in command:
            pyautogui.press('volumeup')
            console.print("Increasing volume...", style="bold blue")
        elif 'down' in command:
            pyautogui.press('volumedown')
            console.print("Decreasing volume...", style="bold blue")
        elif 'mute' in command:
            pyautogui.press('volumemute')
            console.print("Muting volume...", style="bold blue")
        elif 'unmute' in command:
            pyautogui.press('volumemute')
            console.print("Unmuting volume...", style="bold blue")
    elif 'tell me about' in command:
        topic = command.replace('tell me about', '').strip()
        response = ask_gpt(f"Tell me about {topic}")
        console.print(Panel(response, title=f"About {topic}", style="bold cyan"))
    elif 'generate image of' in command:
        prompt = command.replace('generate image of', '').strip()
        image_url = generate_image(prompt)
        console.print(f"Generated image for {prompt}. Check your browser at {image_url}.", style="bold magenta")
    elif 'play music' in command:
        song_query = command.replace('play music', '').strip()
        play_music(song_query)
    elif 'weather' in command:
        location = command.replace('weather', '').strip()
        weather_info = get_weather(location)
        console.print(Panel(weather_info, title=f"Weather in {location}", style="bold blue"))
    elif 'joke' in command:
        joke = get_joke()
        console.print(Panel(joke, title="Joke of the Day", style="bold green"))
    elif 'set reminder' in command:
        reminder_details = command.replace('set reminder', '').strip()
        set_reminder(reminder_details)
    elif 'quit' in command or 'exit' in command:
        console.print("Goodbye!", style="bold red")
        exit()
    else:
        response = ask_gpt(command)
        console.print(Panel(response, title="Hagrid", style="bold cyan"))

openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        return f"Error: {str(e)}"

def play_music(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    console.print(f"Playing music: {query}", style="bold yellow")

def get_weather(location):
    try:
        api_key = os.getenv('WEATHER_API_KEY')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        weather_data = response.json()

        if weather_data.get('cod') != 200:
            return "Location not found."

        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        weather_info = (
            f"Description: {description.capitalize()}\n"
            f"Temperature: {temp}°C (Feels like {feels_like}°C)\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        return weather_info
    except Exception as e:
        return f"Error: {str(e)}"

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        joke_data = response.json()
        joke = f"{joke_data['setup']} - {joke_data['punchline']}"
        return joke
    except Exception as e:
        return f"Error: {str(e)}"

def set_reminder(details):
    try:
        reminder_time, message = details.split(' ', 1)
        reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M").time()
        console.print(f"Reminder set for {reminder_time}: {message}", style="bold blue")

        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= reminder_time:
                console.print(Panel(f"Reminder: {message}", title="Reminder", style="bold red"))
                break
            time.sleep(30)
    except Exception as e:
        console.print(f"Error: {str(e)}", style="bold red")

def main():
    console.print(Panel("Welcome to Hagrid, your personal assistant!", title="Hagrid", style="bold green"))
    while True:
        command = get_user_input()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
