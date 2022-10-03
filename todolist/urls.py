from django.urls import path
from todolist.views import *

app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name="register"),
    path('create-task/', create_task, name="create_task"),
    path('logout/', logout_user, name="logout"),
    path('done/<int:id>', done_task, name='done_task'),
    path('not_done/<int:id>', not_done_task, name='not_done_task'),
    path('delete/<int:id>', delete_task, name='delete_task'),
]
