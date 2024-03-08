from rest_framework import serializers
from .models import Menu

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        method = Menu
        fields = ('name', 'price', 'created', 'updated', 'id')
        read_only_fields = ('created', 'updated', 'id')