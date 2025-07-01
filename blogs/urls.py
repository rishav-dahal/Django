from django.urls import path 
from . views import BlogsView ,CommentsView ,BlogDetailView ,CommentDetailView
urlpatterns = [
   path('blogs/', BlogsView.as_view()),
   path('comments/', CommentsView.as_view()),
   path('blogs/<int:pk>', BlogDetailView.as_view()),
   path('comments/<int:pk>', CommentDetailView.as_view()),
]
