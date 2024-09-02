from django.views.generic import ListView, CreateView, UpdateView, DeleteView, RedirectView
from django.urls import reverse_lazy

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.order_by('is_done', '-created_at')


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('home')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('home')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('home')


class TaskToggleCompleteView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=self.kwargs['pk'])
        task.is_done = not task.is_done
        task.save()
        return super().get(request, *args, **kwargs)


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.order_by('name')


class TagCreateView(CreateView):
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('tag-list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('tag-list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'todo/tag_confirm_delete.html'
    success_url = reverse_lazy('tag-list')
