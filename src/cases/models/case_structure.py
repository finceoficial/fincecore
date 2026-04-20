from django.db import models

class Case(models.Model):
    class PaymentType(models.TextChoices):
        FIXED = "FIXED"
        INSTALLMENT = "INSTALLMENT"
        SUCCESS_FEE = "SUCCESS_FEE"
        HYBRID = "HYBRID"

    firm = models.ForeignKey("firms.Firm", on_delete=models.CASCADE, related_name="cases")

    client_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    total_fee = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices)

    win_probability = models.FloatField(default=1.0)

    stage = models.CharField(max_length=100, null=True, blank=True)

    expected_close_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
