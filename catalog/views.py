from typing import Any

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from catalog.forms import TaskForm, TagForm
from catalog.models import Task, Tag


@login_required()
def home_page(request) -> None:
    tasks = Task.objects.all()
    return render(request, "catalog/home.html", {"tasks": tasks, "current-path": request.path})


class TagListView(generic.View):
    model = Tag

    @staticmethod
    def get(request: Any) -> None:
        tags = Tag.objects.all()
        return render(request, "catalog/tag_list.html", {"tags": tags})


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tag-list")


class TaskListView(generic.View):
    model = Task

    @staticmethod
    def get(request: Any) -> None:
        task = Task.objects.all()
        return render(request, "catalog/task_list.html", {"task": task})


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = "catalog:task-list"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")


class CompleteUndoTaskView(generic.View):
    @staticmethod
    def get(request, pk) -> None:
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse("home"))


def add_task(request) -> None:
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm
    return render(request, "catalog/add_task.html", {"form": form})
