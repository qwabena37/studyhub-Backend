from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Comment.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
