from django.urls import path
from .views import CommentListCreateView

urlpatterns = [
    path("", CommentListCreateView.as_view(), name="comment-list-all"),
    path("<int:project_id>/", CommentListCreateView.as_view()),
]
