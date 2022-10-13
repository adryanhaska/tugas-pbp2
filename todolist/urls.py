from django.urls import path
from todolist.views import *

app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name="register"),
    path('create-task/', create_task, name="create_task"),
    path('logout/', logout_user, name="logout"),
    path('update/<int:id>', update_task, name="update_task"),
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add_todolist_item, name='add_todolist_item')
]
