[app]
title = YTTrimmer
package.name = yttrimmer
package.domain = org.example

source.include_exts = py,kv
assets = assets

requirements = kivy==2.3.0,python3,hostpython3
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
