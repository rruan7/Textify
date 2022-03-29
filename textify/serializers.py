from rest_framework import serializers
from .models import Textify

class TextifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Textify
        fields = ('id', 'title', 'text', 'image')