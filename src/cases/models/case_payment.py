from django.db import models
from ..models.case_structure import Case

class CasePaymentSchedule(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="schedules")

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expected_date = models.DateField()

    probability = models.FloatField(default=1.0)

    paid = models.BooleanField(default=False)