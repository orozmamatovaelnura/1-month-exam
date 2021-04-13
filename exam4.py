import telebot


bot = telebot.TeleBot('')#your token

@bot.message_handler(content_types=['text'])

def send_text(message):
    text1=message.text
    vowels=['a','e','u','i','o']
    calc={'a':0,'e':0,'u':0,'i':0,'o':0}
    for i in text1:
        if i.lower() in vowels:
            calc[i]+=1
    for letter in calc:
        bot.send_message(message.chat.id, f'Letter {letter} repeats {calc[letter]} times')

bot.polling()