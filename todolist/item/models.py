from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
