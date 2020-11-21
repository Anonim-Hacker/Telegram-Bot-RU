import telebot

bot = telebot.TeleBot('1423798151:AAFSabDxxfYdgxN9y9rAZekuc7zcvD6wXWw')

@bot.message_handler(commands=['hello'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'вася дай дз':
        bot.send_message(message.chat.id, 'У меня пока нет данных о ДЗ')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Давай до свидания!')



bot.polling()