from django.db import models
from users.models import Student

class Settlement(models.Model):
    PAYMENT_STATUS = [("PENDING", "Pending"), ("COMPLETED", "Completed")]
    
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="PENDING")
    settlement_method = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="settlements_paid")
    paid_to = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="settlements_received")

    def __str__(self):
        return f"{self.paid_by} → {self.paid_to}: {self.amount}"