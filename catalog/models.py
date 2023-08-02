from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
    )
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.content
