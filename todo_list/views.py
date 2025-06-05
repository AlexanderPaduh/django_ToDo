from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import ToDoItem
from django.views.generic import TemplateView, ListView


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()
    return render(request,
                  template_name="todo_list/index.html",
                  context={"todo_items": todo_items})


class ToDoListIndexView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        context ["todo_items"]: [todo_items] = ToDoItem.objects.all()
    template_name = "todo_list/index.html"


class ToDoListView(ListView):
    # template_name = "todo_list/index.html"
    model = ToDoItem
    # context_object_name = "todo_items"
    def get_context_data(self, **kwargs):
        print(ToDoItem._meta.app_label)
        print(ToDoItem._meta.model_name)
        return super().get_context_data(**kwargs)
