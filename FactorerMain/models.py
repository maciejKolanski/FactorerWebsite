from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class UserData(models.Model):
    login = models.CharField(max_length=45, primary_key=True)
    mail = models.EmailField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.login


class Algorithm(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    CANCELLED_STATUS = -1
    UNDONE_STATUS = 0
    WORKING_STATUS = 1
    DONE_STATUS = 2
    STATUS_CHOICES = (
        (CANCELLED_STATUS, "Cancelled"),
        (UNDONE_STATUS, "Undone"),
        (WORKING_STATUS, "Working"),
        (DONE_STATUS, "Done")
    )

    number_to_factor = models.CharField(max_length=200)
    job_date = models.DateField(default=timezone.now)
    state = models.IntegerField(choices=STATUS_CHOICES, default=UNDONE_STATUS)
    priority = models.IntegerField(default=0)
    result = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number_to_factor)


# class Element(models.Model):
#     first_factor = models.CharField(max_length=200)
#     second_factor = models.CharField(max_length=200)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.task.number_to_factor)
