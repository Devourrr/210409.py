# '''파이썬 300제 201~210'''
# # "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# def print_coin():
#     print("비트코인")

# print_coin()

# for i in range(100):
#     print_coin()

# def print_coins():
#     for i in range(100):
#         print("비트코인")

# print_coins()

# def message():
#     print("A")
#     print("B")
# message()
# print("C")
# message()

# pip install pyTelegramBotAPI

import telebot
TOKEN = '1795391045:AAFsmAKo_ResztkMR96grDLq-Ftyf1luPmY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help']) #/start 또는 /help라는 채팅이 오면 실행
def send_welcome(message):
    print(message)
    bot.reply_to(message, 'Hi there.') # 봇이 응답하는 텍스트

@bot.message_handler(commands=['start','help'])
bot.polling # 주인님의 명령을 기다림
