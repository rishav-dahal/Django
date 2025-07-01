from django.urls import path
from . views import studentsView ,studentDetailView

urlpatterns = [
    path('students/',studentsView,name="liststudents"),
    path('students/<int:pk>/',studentDetailView,name="studentdetail")
]
