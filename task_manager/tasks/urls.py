from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('task/<int:task_id>/', show_task),
    path('task/create/', create_task),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('user/show/<int:user_id>/', show_user)
]