# cradlecare/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # --- INCLUDE THE URLS FROM THE 'tracker' APP ---
    path('', include('tracker.urls')),
]
