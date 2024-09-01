from django.views.generic import ListView

from todo.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'task-list'


class TagListView(ListView):
    model = Tag
    template_name = 'todo/tag_list.html'
    context_object_name = 'tag-list'
