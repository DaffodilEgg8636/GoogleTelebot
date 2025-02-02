import telebot
import requests

# Replace with your own values
API_TOKEN = '7501130877:AAFutHyr8BqqyWukFNqZL5IP8hchRIgs6ME'
SERPAPI_KEY = "445e81af4ed5cbab00b70dc15dcffbdbc7af2e462ddd171cf15c10744ad9559d"

bot = telebot.TeleBot(API_TOKEN)

# Function to perform a Google search using SerpApi
def google_search(query):
    url = f"https://serpapi.com/search?q={query}&api_key={SERPAPI_KEY}"
    response = requests.get(url)
    search_results = response.json()
    
    if 'organic_results' in search_results:
        return search_results['organic_results']
    else:
        return []

# Command handler for /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello! Send me anything you'd like to search for, and I'll fetch the results for you.")

# Command handler for user queries
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    query = message.text
    bot.reply_to(message, "Searching for: " + query)
    
    results = google_search(query)
    
    if results:
        # Send the first 5 results to the user
        for item in results[:5]:
            bot.send_message(message.chat.id, f"{item['title']}\n{item['link']}")
    else:
        bot.send_message(message.chat.id, "Sorry, I couldn't find any results.")

# Start the bot
bot.polling()
