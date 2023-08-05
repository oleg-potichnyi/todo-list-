from django.urls import path

from catalog import views
from catalog.views import (
    TagListView,
    TaskUpdateView,
    TaskDeleteView,
    CompleteUndoTaskView,
    TagUpdateView,
    TagDeleteView,
    TaskListView,
    TagCreateView,
    TaskCreateView,
)

urlpatterns = [
    path("", views.home_page, name="task-list"),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
    path("task-list/", TaskListView.as_view(), name="task-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path(
        "task/<int:pk>/complete-undo/",
        CompleteUndoTaskView.as_view(),
        name="complete_undo_task",
    ),
    path("task/add/", views.add_task, name="add_task"),
    path("tag/add/", views.add_tag, name="add_tag"),
]

app_name = "catalog"
