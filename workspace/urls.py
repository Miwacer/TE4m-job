from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskTypeListView,
    TaskCreateView,
    PositionListView,
    WorkerListView,
    WorkerDetailView,
    PositionDetailView,
    TaskTypeDetailView,
    TeamListView,
    TeamCreateView,
    TeamDeleteView,
    TeamDetailView,
    TeamUpdateView,
    ProjectListView,
    ProjectCreateView,
    ProjectDetailView,
    delete_member_from_team,
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
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("team/<int:pk>", TeamDetailView.as_view(), name="team-detail"),
    path("team/create/", TeamCreateView.as_view(), name="team-create"),
    path("team/<int:pk>/update", TeamUpdateView.as_view(), name="team-update"),
    path("team/<int:pk>/delete", TeamDeleteView.as_view(), name="team-delete"),
    path("remove-member/<int:team_id>/<int:member_id>/", delete_member_from_team, name="remove-member"),
]