from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
import threading
import bot_control

class MainScreen(Screen):
    pass

class RemoteControlApp(MDApp):
    def build(self):
        # Menjalankan Bot Telegram di jalur berbeda (Thread)
        # agar aplikasi HP tetap bisa dibuka
        threading.Thread(target=bot_control.start_bot, daemon=True).start()
        return MainScreen()

if __name__ == '__main__':
    RemoteControlApp().run()
