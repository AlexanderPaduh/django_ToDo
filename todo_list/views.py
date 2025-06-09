from dataclasses import fields

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View

from .forms import TodoItemCreateForm, TodoItemUpdateForm, TodoItemDeleteForm
from .models import ToDoItem
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()[0:1]
    return render(request,
                  template_name="todo_list/index.html",
                  context={"todo_items": todo_items})


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[0:3]
    #     context = super().get_context_data(**kwargs)
    #     return context
    #     context ["todo_items"]: [todo_items] = ToDoItem.object.all()


class ToDoListView(ListView):
    # template_name = "todo_list/index.html"
    model = ToDoItem
    # context_object_name = "todo_items"


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    model = ToDoItem


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = TodoItemCreateForm
    # fields = ("title","description")
    # success_url = revere

class ToDoDeleteView(DeleteView):
    model = ToDoItem


class TodoItemUpdateView(UpdateView):
    model = ToDoItem
    form_class = TodoItemUpdateForm
    template_name_suffix = '_update_form'

class TodoItemDeleteView(DeleteView):
    model = ToDoItem
    form_class = TodoItemDeleteForm
