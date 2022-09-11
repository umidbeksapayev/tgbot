
from translate import translatee
import telebot
TOKEN="5604363807:AAHt6hIwYK8AxE8p6VN90T6ABU70Dp53LCc"
tarjimonbot=telebot.TeleBot(token=TOKEN)
@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar="Assalumu alaykum , botga xush kelibsiz."
    xabar += '\nMatningizni kiriting.'
    tarjimonbot.reply_to(message,xabar)
@tarjimonbot.message_handler(func=lambda msge :  msge.text is not None)
def tarjima(message):
    msge=message.text
    tarjimonbot.reply_to(message,translatee(msge))

tarjimonbot.polling()