from rest_framework import serializers
from .models import ModulesDetail


class ModulesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModulesDetail
        fields = ['id', 'modules', 'week', 'description']