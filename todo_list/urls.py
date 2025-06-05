from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "todo_list"

urlpatterns = [
    # path("", views.index_view, name="index"),
    # path("", views.ToDoListIndexView.as_view())
    path("", views.ToDoListView.as_view(), name="index"),

]
