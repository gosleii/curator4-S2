import telebot

bot = telebot.TeleBot('6604283252:AAFyighGf9Fot1BKLlD2Nk1RBNfibnjwKq4')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'добрый вечер! напиши, какое у тебя настроение, а я тебе посоветую, что скушать под такое настроение!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['sad'])
def main(message):
    bot.send_message(message.chat.id, 'думаю, что хинкали замечательно поднимут тебе настроение!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['not_bad'])
def main(message):
    bot.send_message(message.chat.id,
                     'я рада, что у тебя все не так плохо, как могло бы быть. порадуй себя сегодня хачапури по-аджарски!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['fine'])
def main(message):
    bot.send_message(message.chat.id,
                     'это здорово, что у тебя все хорошо! получи еще одну дозу легких эндорфинов, съев кусочек торта',
                     parse_mode='Markdown')


@bot.message_handler(commands=['good'])
def main(message):
    bot.send_message(message.chat.id,
                     'думаю, у тебя в жизни все идет в гору, так что съешь что-то легкое, напрмер, салат Капрезе',
                     parse_mode='Markdown')


bot.infinity_polling()