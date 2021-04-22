import telebot
import random

bot = telebot.TeleBot('1767181911:AAHCpGTTxlqcIfYNAGGPhYTSOnsUYtOR7d0')
wordlist = {'Черный': ('Juodas', 'Černý'),'Синий': ('Mėlynas', 'Modrý'), 
            'Коричневый': ('Rudas', 'Hnědý'), 'Зеленый': ('Žalias', 'Zelený'), 
            'Оранжевый': ('Oranžinis', 'Oranžový'), 'Фиолетовый': ('Violetinis', 'Purpurový'),
            'Красный': ('Raudonas', 'Červený'), 'Розовый': ('Rožinė', 'Růžový'), 
            'Желтый': ('Geltona', 'Žlutý'), 'Серый': ('Pilka', 'Šedý'), 'Белый': ('Balta', 'Bílý')}
klic = '1'
klic2 = '2'

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text != '/start':
        bot.send_message(message.from_user.id, "я тебя не понимаю")
    else:
        global klic
        global klic2
        klic, klic2 = gogo()
        msg = bot.send_message(message.chat.id, klic)
        bot.register_next_step_handler(msg, get_answer)

def gogo():
    kl = random.choice(list(wordlist.keys()))
    kl2 = wordlist[kl]
    return (kl, kl2)

def get_answer(message):
    global klic2
    answer = message.text
    if answer in klic2:
        bot.send_message(message.chat.id, 'right!')
    else:
        bot.send_message(message.chat.id, 'no. it must be ' + klic2[0] + ' or ' + klic2[1])

bot.polling(none_stop=True, interval=0)
