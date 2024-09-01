from django.urls import path
from . import views
from .views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("/tags/", views.TagListView.as_view(), name="tag")
]
