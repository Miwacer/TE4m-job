from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Task, TaskType, Worker, Position


def index(request: HttpRequest) -> HttpResponse:
    user = request.user

    context = {
        "user": user,
    }
    return render(request, 'workspace/index.html', context)


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task