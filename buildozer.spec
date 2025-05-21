[app]
# App metadata
title               = YTTrimmer
package.name        = yttrimmer
package.domain      = org.example
version             = 1.0.0
source.dir          = .

# Force an APK (not AAB)
android.release_artifact = apk

# What to include
source.include_exts = py,kv
android.copy_assets = assets

# Python deps
requirements        = kivy==2.3.0,httplib2

# Tell Buildozer to use the SDK you installed in CI
android.sdk_path    = /home/runner/android-sdk

# Let p4a download NDK r25b
android.ndk         = 25b

# Android settings
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api         = 33
android.minapi      = 24
android.build_tools = 36.0.0
android.archs       = arm64-v8a
