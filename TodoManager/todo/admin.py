from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'deadline', 'is_done')
    search_fields = ('content',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    # Add additional fields and filters as needed
