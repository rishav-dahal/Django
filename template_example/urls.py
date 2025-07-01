from django.urls import path
from .views import index , user_list , form_name_view , users

urlpatterns = [
    path('', index, name='index'),
    path('user_list/', user_list, name='user_list'),
    path('form/', form_name_view, name='form_name_view'),
    path('signup/', users, name='signup'),

]

