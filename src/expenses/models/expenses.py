from django.db import models

class Expense(models.Model):
    class Frequency(models.TextChoices):
        ONE_TIME = "ONE_TIME"
        MONTHLY = "MONTHLY"
        YEARLY = "YEARLY"

    firm = models.ForeignKey("firms.Firm", on_delete=models.CASCADE, related_name="expenses")

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    due_date = models.DateField()

    frequency = models.CharField(max_length=20, choices=Frequency.choices, default=Frequency.ONE_TIME)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
