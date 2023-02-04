from rest_framework import serializers
from main.models import User

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')