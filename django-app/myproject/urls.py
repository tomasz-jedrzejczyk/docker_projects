# Project-level urls.py (update the imports/paths to match your project)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

# IMPORTANT: handler404 must be set at module level of the root urls.py
# Point the 404 handler to the `home` app's custom_404 view.
handler404 = 'home.views.custom_404'
