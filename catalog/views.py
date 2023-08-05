from typing import Any

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from catalog.forms import TaskForm, TagForm
from catalog.models import Task, Tag


def home_page(request) -> None:
    tasks = Task.objects.all()
    return render(request, "catalog/task_list.html", {"tasks": tasks, "current-path": request.path})


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
    def get(request, *args, **kwargs) -> None:
        tasks = Task.objects.order_by('-is_done', '-create_at')
        return render(request, "catalog/task_list.html", {"tasks": tasks})


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")


class CompleteUndoTaskView(generic.View):
    @staticmethod
    def get(request, pk) -> None:
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse("catalog:task-list"))


def add_task(request) -> None:
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalog:task-list")
    else:
        form = TaskForm
    return render(request, "catalog/add_task.html", {"form": form})


def add_tag(request) -> None:
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalog:tag-list")
    else:
        form = TagForm
    return render(request, "catalog/add_tag.html", {"form": form})
