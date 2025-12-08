from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Collaboration
from .serializers import CollaborationSerializer

class JoinProjectView(generics.CreateAPIView):
    serializer_class = CollaborationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
