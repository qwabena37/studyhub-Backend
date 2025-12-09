from django.urls import path
from .views import CommentListCreateView

urlpatterns = [
    path("<int:project_id>/", CommentListCreateView.as_view()),
]
