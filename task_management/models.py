from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):

    def __str__(self):
        return self.username


class Tasks(models.Model):
    PRIORITY_LEVEL = [
        ('LOW', 'low'),
        ('MEDIUM', 'medium'),
        ('HIGH', 'high'),
    ]

    STATUS_TYPES = [
        ('PENDING', 'pending'),
        ('COMPLETED', 'completed')
    ]
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Due_Date = models.DateField()
    Priority_Level = models.CharField(max_length=50, choices=PRIORITY_LEVEL)
    Status = models.CharField(max_length=25, choices=STATUS_TYPES)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.Title
