from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete
from todolist.views import done
from todolist.views import show_todolist_ajax
from todolist.views import submit_ajax, show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='createtask'),
    path('delete/<int:id>/', delete, name='delete'),
    path('done/<int:id>/', done, name='done'),
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'),
    path('/submit', submit_ajax, name='submit_ajax'),
    path('/json', show_json, name='show_json'),
]