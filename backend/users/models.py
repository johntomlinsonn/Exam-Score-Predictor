from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    study_habits = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username

class TestScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='test_scores')
    subject = models.CharField(max_length=100)
    score = models.FloatField()
    study_duration = models.FloatField(help_text="Study duration in hours")
    feeling_before_test = models.FloatField(max_length=100, help_text="Feeling before test (0-100)")
    mistakes_made = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.subject} - {self.score}"