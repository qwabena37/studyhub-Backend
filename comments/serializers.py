from rest_framework import serializers
from .models import Collaboration

class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = ['id', 'user', 'project', 'joined_at']
