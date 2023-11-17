from django.urls import path
from . import views
from .views import TodoAPIView, CreateTodoAPIView, TodoUpdateAPIView

urlpatterns = [
    path('todo', TodoAPIView.as_view(), name='todo'),
    path('create-todo', CreateTodoAPIView.as_view(), name='create_todo'),
    path('todo-update/<int:pk>', TodoUpdateAPIView.as_view(), name='todo_update'),
]
