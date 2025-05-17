from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
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
def index(request):
    context = {
        'urgent_tasks': Task.objects.filter(priority='UR').order_by('deadline')[:5],
        'projects': Project.objects.all().order_by('-id')[:5],
        'teams': Team.objects.all(),
    }
    return render(request, 'workspace/index.html', context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.all().select_related("task_type")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = (
        Task.objects.all().prefetch_related(
            "assignees__position").select_related("task_type")
    )


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
    queryset = Worker.objects.all().select_related("position")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.all().select_related("position")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    queryset = Project.objects.all().prefetch_related("tasks").select_related("team")


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    queryset = Project.objects.all().select_related("team").prefetch_related("tasks")


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
    queryset = Team.objects.all().prefetch_related("members")


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    queryset = Team.objects.all().prefetch_related("members__position")

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


@login_required
def delete_member_from_team(request, team_id: int, member_id: int):
    team = Team.objects.get(id=team_id)
    team.members.remove(member_id)

    return redirect("workspace:team-detail", team_id)


@login_required
def toggle_status_complete(request, task_id: int, user_id: int):
    task = Task.objects.get(id=task_id)
    task.is_complete = not task.is_complete
    task.save()

    return redirect("workspace:worker-detail", user_id)