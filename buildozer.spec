[app]
# App metadata
title = YTTrimmer
package.name = yttrimmer
package.domain = org.example
version = 1.0.0
source.dir = .

# What to include
source.include_exts = py,kv
android.copy_assets = assets

# Python deps
requirements = kivy==2.3.0,httplib2

# Android settings
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
