from django.urls import path
from . import views

app_name = "todolist"

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_all'),
    path('complete/', views.TodoListComplete.as_view(), name='todo_completed'),
    path('incomplete/', views.TodoListIncomplete.as_view(), name='todo_incompleted'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='todo_detail'),
    path('new', views.TodoCreate.as_view(), name='todo_new'),
    path('edit/<int:pk>/', views.TodoUpdate.as_view(), name='todo_update'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='todo_delete'),
]