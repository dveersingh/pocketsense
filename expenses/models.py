
from django.db import models
from users.models import Student
from groups.models import Group
from categories.models import Category

class Expense(models.Model):
    SPLIT_TYPES = [("EQUAL", "Equal"), ("UNEQUAL", "Unequal"), ("PERCENTAGE", "Percentage")]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    split_type = models.CharField(max_length=20, choices=SPLIT_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    receipt_image = models.ImageField(upload_to='receipts/', blank=True, null=True)
    paid_by = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='expenses')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='expenses', blank=True, null=True)

    def __str__(self):
        return {self.amount} - {self.category}