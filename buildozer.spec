[app]
# App metadata
title              = YTTrimmer
package.name       = yttrimmer
package.domain     = org.example
version            = 1.0.0
source.dir         = .
# Force Buildozer to generate an APK instead of an AAB
android.release_artifact = apk

# What to include
source.include_exts = py,kv
android.copy_assets= assets

# Python dependencies
requirements       = kivy==2.3.0,httplib2

# Point Buildozer at our CI-installed SDK
android.sdk_path   = /home/runner/android-sdk
android.ndk_path   = /home/runner/.buildozer/android/platform/android-ndk-r25b

# Android settings
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api         = 33
android.minapi      = 24
android.build_tools = 36.0.0
android.archs       = arm64-v8a
