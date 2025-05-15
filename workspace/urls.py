from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskTypeListView,
    PositionListView,
    WorkerListView,
    WorkerDetailView,
    TaskCreateView,
    PositionDetailView,
    TaskTypeDetailView,
    ProjectListView,
    ProjectCreateView,
    ProjectDetailView,
)


app_name = "workspace"
urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path(
        "task-type/<int:pk>",
         TaskTypeDetailView.as_view(),
         name="task-type-detail"
    ),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>", PositionDetailView.as_view(), name="position-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("project/create/", ProjectCreateView.as_view(), name="project-create"),
    path("project/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),
]