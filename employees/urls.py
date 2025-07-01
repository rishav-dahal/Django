from django.urls import path , include
from . views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', EmployeeViewset, basename='employee')

urlpatterns = [
   # path('employees/',Employees.as_view()),
   # path('employees/<int:pk>/',EmployeesDetails.as_view()),
   path('',include(router.urls))
]
