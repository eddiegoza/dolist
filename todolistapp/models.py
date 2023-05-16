from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7) 


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    auto_delete_date = models.DateTimeField(default=one_week_hence)
    due_date = models.DateField(null=True)
    due_time = models.TimeField(null=True)
    set_reminder= models.TimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
