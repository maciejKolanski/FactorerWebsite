from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

class Algorithm(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    number_to_factor = models.BigIntegerField()
    job_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number_to_factor)

class Element(models.Model):
    first_factor = models.BigIntegerField()
    second_factor = models.BigIntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)