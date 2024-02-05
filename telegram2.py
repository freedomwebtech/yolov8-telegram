import telepot

# Insert your telegram token below
bot_token = '6738497767:AAEwPts6HDxCXTOA8d5MIuHXjrR5CgMfXhQ'
bot = telepot.Bot(bot_token)

# Get updates to retrieve the latest messages
updates = bot.getUpdates()

# Check if there are any updates
if updates:
    # Extract the chat ID from the latest update
    chat_id = updates[-1]['message']['chat']['id']
    print(f"Chat ID: {chat_id}")
else:
    print("No updates found. Send a message to the bot first to generate an update.")
