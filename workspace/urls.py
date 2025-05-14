from django.urls import path
from .views import (
    index,
TaskListView,
TaskDetailView,

)


app_name = "workspace"
urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
]