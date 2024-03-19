from rest_framework import serializers
from .models import Menu  # Import the Menu model

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__' # You can also specify fields individually
