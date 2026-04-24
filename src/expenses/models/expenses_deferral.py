from django.db import models
from src.expenses.models.expenses import Expense

class ExpenseDeferral(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="deferrals")

    original_date = models.DateField()
    new_date = models.DateField()

    penalty_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)