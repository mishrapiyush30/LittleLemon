# restaurant/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet,msg
from rest_framework.authtoken.views import obtain_auth_token


# Creating a router and registering our ViewSets with it.
router = DefaultRouter()
router.register(r'booking', BookingViewSet, basename='booking')

# Additional urlpatterns can be added that aren't handled by the router.
urlpatterns = [
    path('menu/', MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
    # Including router URLs
    path('', include(router.urls)),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
