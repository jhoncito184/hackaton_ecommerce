from rest_framework import serializers
from .models import Postulations


class PostulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulations
        fields = ['id', 'username', 'phone', 'email', 'product']