import telegram


# token = '5349567076:AAF4aCMkTXMotHPuQ02-YE9J0Q5gXu-XKH9MA'
token = '5349567076:AAF4aCMkTXMotHPuQ02YE9J0Q5gXuXKH9MA'
bot = telegram.Bot(token=token)

bot.send_message(chat_id='1692132404', text='[哔哩哔哩](不要啊)',parse_mode=telegram.ParseMode.MARKDOWN)
print("Successful")
