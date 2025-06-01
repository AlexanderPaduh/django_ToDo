from django.contrib import admin

from todo_list.models import ToDoItem

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
  list_display = 'title','done'

  def __str__(self):
      return f"{self.title} - {self.done}"