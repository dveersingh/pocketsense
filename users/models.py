
from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    college = models.CharField(max_length=100)
    semester = models.IntegerField(default=1)
    default_payment_methods = models.JSONField(default=list)
    upi_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username