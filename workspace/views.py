from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Task, TaskType, Worker, Position


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
    fields = [
        "name",
        "description",
        "deadline",
        "priority",
        "task_type",
        "assignees",
    ]

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

