from django import forms

from todo_list.models import ToDoItem


class TodoItemCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('title','description','done',)
        widgets = {
            "description":forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        }
        help_texts = {
            "description":"Some useful description",
        }


class TodoItemUpdateForm(forms.ModelForm):
    class Meta(TodoItemCreateForm.Meta):
        fields = ('title',
                  'description',
                  'done',)

class TodoItemDeleteForm(forms.ModelForm):
    class Meta(TodoItemCreateForm.Meta):
        fields = ('title',)
