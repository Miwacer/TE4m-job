from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm, TeamForm
from .models import (
    Task,
    TaskType,
    Worker,
    Position,
    Project,
    Team,
)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    user = request.user

    context = {
        "user": user,
    }
    return render(request, 'workspace/index.html', context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("workspace:task-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "workspace/task_type_list.html"



class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "workspace/type_task_detail.html"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = [
        "name",
        "description",
        "team",
        "tasks",
    ]
    success_url = reverse_lazy("workspace:project-list")


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class TeamDeleteView(generic.DeleteView):
    model = Team
    success_url = reverse_lazy("workspace:team-list")


class TeamUpdateView(generic.UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("workspace:team-list")


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("workspace:team-list")