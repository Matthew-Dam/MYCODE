# multi_system.py
import os
import re
import datetime
from datetime import date, timedelta
from colorama import Fore, Style, init as colorama_init
from requests.exceptions import ConnectionError, RequestException
import google.genai as genai
from openai import OpenAI
import textwrap
import sys
import time
import requests
import json

from dotenv import load_dotenv

# Load .env file
import sys
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'APIs.env')
load_dotenv(env_path)

# Access your keys
openai_key = os.getenv("OPENAI_API_KEY")
news_key = os.getenv("NEWS_API_KEY")
weather_key = os.getenv("WEATHER_API_KEY")

colorama_init(autoreset=True)  # auto-reset colors after prints

# Doubly linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly linked list for app navigation
class ReqLink:
    def __init__(self):
        self.starting = None
        self.current = None

    def append(self, data):
        new_node = Node(data)
        if self.starting is None:
            self.starting = new_node
            self.current = new_node
        else:
            last = self.starting
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.starting:
            new_node.next = self.starting
            self.starting.prev = new_node
            self.starting = new_node
            # keep current where it was
        else:
            self.starting = new_node
            self.current = new_node

    def move_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        print(Fore.YELLOW + "No next app.")
        return None

    def move_backward(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        print(Fore.YELLOW + "No previous app.")
        return None

# Main request handling class
class Request:
    def __init__(self):
        # Read API keys from environment variables for safety
        self.openai_api = os.getenv("OPENAI_API_KEY")
        self.gemini_api = os.getenv("GEMINI_API_KEY")
        self.news_api = os.getenv("NEWS_API_KEY") # newsapi.org
        self.weather_api = os.getenv("WEATHER_API_KEY") # openweathermap.org

        if not self.openai_api:
            print(Fore.RED + "Warning: OPENAI_API_KEY not set. OpenAI features will fail if used.")
        if not self.gemini_api:
            print(Fore.YELLOW + "Warning: GEMINI_API_KEY not set. Gemini chat will fail if used.")
        if not self.news_api:
            print(Fore.YELLOW + "Warning: NEWS_API_KEY not set. News will fail if used.")
        if not self.weather_api:
            print(Fore.YELLOW + "Warning: WEATHER_API_KEY not set. Weather will fail if used.")

        # initialize OpenAI client only if key present
        try:
            if self.openai_api:
                self.client = OpenAI(api_key=self.openai_api)
            else:
                self.client = None
        except Exception:
            self.client = None

    def search(self):
        """DuckDuckGo instant answer search (console)"""
        try:
            while True:
                user_search = input(Fore.LIGHTYELLOW_EX + "\nEnter a keyword to search for (or 'exit' to quit): ").strip()
                if user_search.lower() in {"exit", "quit"}:
                    print(Fore.CYAN + "Goodbye...")
                    break

                url = "https://api.duckduckgo.com/"
                params = {"q": user_search, "format": "json", "no_redirect": 1, "no_html": 1}
                try:
                    response = requests.get(url, params=params, timeout=8)
                    response.raise_for_status()
                    data = response.json()
                except RequestException as e:
                    print(Fore.RED + f"Search request failed: {e}")
                    continue
                result_lines = []

                if data.get("AbstractText"):
                    result_lines.append(f"Definition: {data['AbstractText']}")
                    if data.get("AbstractURL"):
                        result_lines.append(f"Source: {data['AbstractURL']}")
                else:
                    # RelatedTopics can be list of dicts or nested topics
                    related = data.get("RelatedTopics") or []
                    count = 0
                    for topic in related:
                        if count >= 7:
                            break
                        if "Text" in topic:
                            result_lines.append("Info: " + topic["Text"])
                            if "FirstURL" in topic:
                                result_lines.append("Link: " + topic["FirstURL"])
                            count += 1
                        elif "Topics" in topic:  # nested
                            for t in topic["Topics"]:
                                if count >= 7:
                                    break
                                if "Text" in t:
                                    result_lines.append("Info: " + t["Text"])
                                    if "FirstURL" in t:
                                        result_lines.append("Link: " + t["FirstURL"])
                                    count += 1

                if not result_lines:
                    print(Fore.YELLOW + "No results found.")
                else:
                    print("\n" + "\n".join(result_lines))
                    input(Fore.GREEN + "\nPress Enter to continue searching...")

        except KeyboardInterrupt:
            print("\n" + Fore.CYAN + "Search interrupted by user. Returning to menu.")

    def chat(self):
        """Gemini chat using google.genai"""
        if not self.gemini_api:
            print(Fore.RED + "Gemini API key not available. Please set GEMINI_API_KEY.")
            return
        try:
            client = genai.Client(api_key=self.gemini_api)
            
        except Exception as e:
            print(Fore.RED + f"Failed to initialize Gemini client: {e}")
            return

        try:
            while True:
                user_input = input(Fore.LIGHTBLUE_EX + "\nYou: ").strip()
                if user_input.lower() in ["exit", "quit"]:
                    print(Fore.CYAN + "Enjoy your present — goodbye.")
                    break
                try:
                    
                    
                    # Generate response
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=user_input,
                        config=genai.types.GenerateContentConfig(temperature=0.7)
                    )
                    
                    ai_response = response.text if response.text else "No response"
                    
                    
                    out_come = "AI: " + ai_response
                except Exception as e:
                    out_come = f"AI (error): {e}"

                wrapped_text = textwrap.fill(out_come, width=70)
                for char in wrapped_text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print()  # newline after the slow-print
        except KeyboardInterrupt:
            print("\n" + Fore.CYAN + "Chat interrupted. Returning to menu.")

    def daily_news(self):
        """Fetch news from NewsAPI (newsapi.org)"""
        if not self.news_api:
            print(Fore.RED + "News API key not set. Please set NEWS_API_KEY.")
            return

        url = "https://newsapi.org/v2/everything"
        try:
            while True:
                today = date.today()
                yesterday = today - timedelta(days=1)
                search = input(Fore.CYAN + "\nSearch for daily news (or 'exit' to quit): ").strip()
                if search.lower() in {"exit", "quit"}:
                    print(Fore.LIGHTCYAN_EX + "Hope you got the news you wanted. Returning to menu.")
                    break

                params = {
                    "q": search,
                    "from": yesterday.isoformat(),
                    "to": today.isoformat(),
                    "language": "en",
                    "sortBy": "publishedAt",
                    "pageSize": 10,
                    "apiKey": self.news_api,
                }
                try:
                    response = requests.get(url, params=params, timeout=10)
                    if response.status_code != 200:
                        print(Fore.RED + f"Error: {response.status_code} — {response.text}")
                        continue
                    data = response.json()
                except RequestException as e:
                    print(Fore.RED + f"News request failed: {e}")
                    continue

                articles = data.get("articles") or []
                if not articles:
                    print(Fore.YELLOW + "No news articles found for your search.")
                    continue

                print(Fore.BLACK + "\t\t====BREAKING NEWS====")
                for i, article in enumerate(articles[:10], start=1):
                    source_name = (article.get("source") or {}).get("name") or "Unknown source"
                    author = article.get("author") or "Unknown"
                    title = article.get("title") or "No title"
                    description = article.get("description") or ""
                    content_raw = article.get("content") or ""
                    clean_content = content_raw.split("[+")[0] if content_raw else ""
                    url_article = article.get("url") or ""

                    print(Fore.BLUE + f"\n\t\t==== ARTICLE {i} ====")
                    print(Fore.LIGHTYELLOW_EX + "From:", source_name)
                    print(Fore.RED + "Author:", author)
                    print("\nTitle:", title)
                    print(Fore.WHITE + "\nNews:", description)
                    if clean_content:
                        print(Fore.WHITE + "Content:", clean_content)
                    if url_article:
                        print(Fore.LIGHTMAGENTA_EX + "\nURL:" + url_article)
                    print()  # blank line for readability
            if articles:
                input(Fore.GREEN + "Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n" + Fore.CYAN + "News search interrupted. Returning to menu.")

    def get_weather(self):
        """Get current weather using OpenWeatherMap"""
        if not self.weather_api:
            print(Fore.RED + "Weather API key not set. Please set WEATHER_API_KEY.")
            return

        try:
            while True:
                country = input(Fore.WHITE + "Enter country name (or 'exit' to quit, blank = Ghana): ").strip()
                if not country:
                    country = "Ghana"
                if country.lower() in {"exit", "quit"}:
                    print(Fore.CYAN + "Weather check ended. Returning to menu.")
                    break
                city = input(Fore.WHITE + "Enter city name: ").strip()
                if not city:
                    print(Fore.YELLOW + "City required. Try again.")
                    continue

                url = "http://api.openweathermap.org/data/2.5/weather"
                params = {"q": f"{city},{country}", "appid": self.weather_api, "units": "metric"}
                try:
                    response = requests.get(url, params=params, timeout=8)
                    response.raise_for_status()
                    data = response.json()
                except RequestException as e:
                    print(Fore.RED + f"Weather request failed: {e}")
                    continue

                # OpenWeather returns cod as int or string; handle both
                cod = data.get("cod")
                try:
                    cod_int = int(cod)
                except Exception:
                    cod_int = None

                if cod_int != 200:
                    message = data.get("message", "Unknown error")
                    print(Fore.RED + f"Error fetching weather: {message}")
                    continue

                print(Fore.MAGENTA + f"Today's weather in {city.capitalize()}, {country.capitalize()}:\n")
                main = data.get("main") or {}
                weather_list = data.get("weather") or [{}]
                print(Fore.LIGHTBLUE_EX + f"Temperature: {main.get('temp')}°C")
                print(Fore.CYAN + f"Humidity: {main.get('humidity')}%")
                desc = weather_list[0].get("description", "").title()
                print(Fore.YELLOW + f"Conditions: {desc}\n")
                input(Fore.GREEN + "Press Enter to continue...")

        except KeyboardInterrupt:
            print("\n" + Fore.CYAN + "Weather check interrupted. Returning to menu.")


def run():
    print(Fore.BLUE + "=" * 51)
    print(Fore.LIGHTCYAN_EX + "\t\tMULTI - SYSTEM")
    print(Fore.BLUE + "=" * 51)

    applink = ReqLink()
    req = Request()

    # Append function objects (not function call results)
    applink.append(req.get_weather)
    applink.append(req.daily_news)
    applink.append(req.chat)
    applink.append(req.search)

    # show current selection label helper
    def current_label():
        if applink.current and applink.current.data:
            return applink.current.data.__name__
        return "None"

    try:
        while True:
            prompt = (
                Fore.LIGHTGREEN_EX
                + f"\nCurrent app: {current_label()}\n"
                + "1. Run current app\n2. Next app\n3. Previous app\n4. Exit\n> "
            )
            choice = input(prompt).strip()
            if choice == "1":
                if applink.current and applink.current.data:
                    # Call the function
                    applink.current.data()
                else:
                    print(Fore.RED + "No app selected yet.")
            elif choice == "2":
                next_app = applink.move_forward()
                if next_app:
                    print(Fore.CYAN + f"Switched to next app: {applink.current.data.__name__}")
            elif choice == "3":
                prev_app = applink.move_backward()
                if prev_app:
                    print(Fore.CYAN + f"Switched to previous app: {applink.current.data.__name__}")
            elif choice == "4":
                print(Fore.CYAN + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Enter 1, 2, 3 or 4.")
    except KeyboardInterrupt:
        print("\n" + Fore.CYAN + "Exiting. Goodbye.")


if __name__ == "__main__":
    run()