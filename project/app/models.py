from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, null=True, blank=True)

class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    assignees = models.ManyToManyField(User, blank=True)

class Bug(models.Model):
    issue_no = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    date_created = models.DateField()
    date_resolved = models.DateField(null=True, blank=True)
    feature = models.CharField(max_length=100, null=True, blank=True)
    steps = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, default="Unresolved")
    description = models.TextField(null=True, blank=True)
    discovered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='discovered_by')
    resolved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='resolved_by')