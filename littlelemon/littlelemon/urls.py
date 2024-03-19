# Update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

router = DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include(router.urls)),
    path('restaurant/booking/', include(router.urls)),
]
