from rest_framework import serializers
from .models import MusicWorks

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicWorks
        fields = ['id', 'title', 'contributors', 'iswc']
