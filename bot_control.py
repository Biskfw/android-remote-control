import telebot
import platform
import os

TOKEN = '8229088402:AAFAsQV-fQlzaZYdXSevS1XvOdbfn-p164s'
bot = telebot.TeleBot(TOKEN)

@bot.message_count_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Sistem Remote Aktif! Siap menerima perintah.")

@bot.message_handler(commands=['info'])
def send_info(message):
    info = f"Model: {platform.machine()}\nSistem: {platform.system()}\nVersi: {platform.version()}"
    bot.reply_to(message, info)

def start_bot():
    bot.polling(none_stop=True)
