[app]
title = YTTrimmer
package.name = yttrimmer
package.domain = org.example

# source files & assets
source.include_exts = py,kv
android.copy_assets = assets

# real Python requirements
requirements = kivy==2.3.0,httplib2

# Android settings
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
