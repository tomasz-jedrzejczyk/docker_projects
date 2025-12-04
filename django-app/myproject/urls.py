# Project-level urls.py (update the imports/paths to match your project)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # <-- ensure this points to your home/main app
]

# IMPORTANT: handler404 must be set at module level of the root urls.py
# Replace 'main' with the name of the app that contains the view below.
handler404 = 'main.views.custom_404'
