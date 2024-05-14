from rest_framework import serializers
from .models import Programmer


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'  # o lista los campos que quieres serializar manualmente
