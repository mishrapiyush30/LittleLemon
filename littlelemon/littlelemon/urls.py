# project-level urls.py (e.g., littlelemon/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')), 
    path('auth/', include('djoser.urls')),  # Basic authentication endpoints
    path('auth/', include('djoser.urls.authtoken')),   # This includes both the router URLs and any additional URLs defined in the app.
]
