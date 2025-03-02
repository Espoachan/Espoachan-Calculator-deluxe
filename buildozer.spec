[app]

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,numpy

# (str) Application versioning (method 1)
version = 0.1

# (str) Application name
title = MiAppKivy

# (str) Package name
package.name = com.miappkivy

# (str) Package domain (used for android/ios packaging)
package.domain = org.kivy

[buildozer]

# (int) Log level (0 = quiet, 1 = normal, 2 = verbose)
log_level = 2

# (str) Android NDK version to use
android.ndk = r21e

# (str) Android SDK version to use
android.sdk = 30

# (bool) Copy libraries that are required to run the app (e.g. from site-packages)
# android.copy_libs = True
