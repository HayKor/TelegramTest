import telebot

bot = telebot.TeleBot('5875512828:AAE0kTeKfgSSgMo2rxFkP9Jy9CV2fGDTbo4')


@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = ('Приветствую, <b>Варвара</b>!'
                    ' Этот бот был написан по фану на коленке за буквально 15 минут!! '
                    'Введи "/info"')
    bot.send_message(message.chat.id, welcome_text, parse_mode='html')

@bot.message_handler(commands=['info'])
def info(message):
    user_info = (f'<b>Username</b>: {message.from_user.username}, '
                 f'<b>First Name</b>: {message.from_user.first_name}, '
                 f'<b>Last Name</b>: {message.from_user.last_name}')
    bot.send_message(message.chat.id, user_info, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    gibberish = 'Пожалуйста, пиши четче, ничего не понятно... /info'
    bot.send_message(message.chat.id, gibberish, parse_mode='html')

bot.polling(none_stop=True)
