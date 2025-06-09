from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "todo_list"

urlpatterns = [
    # path("", views.index_view, name="index"),
    path("", views.ToDoListIndexView.as_view(), name="index"),
    path("list/", views.ToDoListView.as_view(), name="list"),
    path("create/", views.ToDoItemCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.TodoItemUpdateView.as_view(), name="update"),
    path("done/", views.ToDoListDoneView.as_view(), name="done"),
    path("<int:pk>/", views.ToDoDetailView.as_view(), name="detail"),

]
