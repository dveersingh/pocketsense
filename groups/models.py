from django.db import models
from users.models import Student

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Student, related_name='group_members')  # Change related_name
    created_by = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='created_groups')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name