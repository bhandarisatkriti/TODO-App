from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    #models.Model : This Python class should behave like a database table
    #  managed by the ORM.
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    