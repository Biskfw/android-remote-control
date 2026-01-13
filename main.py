"""
📱 Android Remote Control - Main Application
Kivy-based app that runs Telegram bot in background
"""
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
import threading
import os
import sys

def start_bot_service():
    """Start Telegram bot service in background"""
    try:
        # Add current directory to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.append(current_dir)
        
        # Import and start bot
        import bot_control
        print("✅ Telegram bot service started successfully")
        
        # Write status file
        with open("/sdcard/omen_status.txt", "w") as f:
            f.write(f"Service active - PID: {os.getpid()}")
            
    except Exception as e:
        # Write error to file
        error_msg = f"Error starting bot: {str(e)}"
        print(error_msg)
        with open("/sdcard/omen_error.txt", "w") as f:
            f.write(error_msg)

class RemoteControlApp(App):
    """Main Kivy application"""
    def build(self):
        # Start bot service in background thread
        service_thread = threading.Thread(target=start_bot_service, daemon=True)
        service_thread.start()
        
        # Create simple UI
        return Label(
            text="System Service\nRunning in background",
            font_size='20sp',
            halign='center'
        )

if __name__ == '__main__':
    RemoteControlApp().run()
