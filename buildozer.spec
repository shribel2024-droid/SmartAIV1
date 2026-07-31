[app]

title = SmartAI
package.name = smartai
package.domain = org.smartai

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Architecture
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET

# Logging
log_level = 2
