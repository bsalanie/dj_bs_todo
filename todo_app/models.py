from django.db import models
from django.urls import reverse
from django.utils import timezone


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    # we don't want two lists with the same title
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):  # returns the URL for this todo list
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # could be left blank
    created_date = models.DateTimeField(auto_now_add=True)  # when the item was created
    due_date = models.DateTimeField(default=one_week_hence)  # when the item is due
    todo_list = models.ForeignKey(
        ToDoList,  # links the ToDoItem back to its ToDoList
        on_delete=models.CASCADE,  # if a to-do list is deleted,
        # then all the associated to-do items will be deleted too
    )

    def get_absolute_url(self):  # returns the URL for this todo item
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):  # for debugging
        return f"{self.title}: due {self.due_date}"

    class Meta:  # used to specify ordering of items in the database
        ordering = ["due_date"]
