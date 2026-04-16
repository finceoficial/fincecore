from django.db import models
from ..models.auth import User

class LawyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    full_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    oab_number = models.CharField(max_length=20)
    oab_state = models.CharField(max_length=2)

    phone = models.CharField(max_length=20)
    office_address = models.TextField(blank=True)

    bank_name = models.CharField(max_length=100, blank=True)
    bank_account = models.CharField(max_length=50, blank=True)

    practice_areas = models.JSONField(default=list)
    years_of_experience = models.IntegerField(null=True, blank=True)

    average_monthly_income = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    average_monthly_expense = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    financial_goal = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    has_employees = models.BooleanField(default=False)
    office_type = models.CharField(max_length=20, choices=[("HOME", "HOME"), ("PHYSICAL", "PHYSICAL")], default="HOME")

    income_variability = models.CharField(max_length=20, choices=[("LOW", "LOW"), ("MEDIUM", "MEDIUM"), ("HIGH", "HIGH")], default="HIGH")

    has_bank_connected = models.BooleanField(default=False)

    goal_type = models.CharField(max_length=20, choices=[("SURVIVAL", "SURVIVAL"), ("STABILITY", "STABILITY"), ("GROWTH", "GROWTH")], default="STABILITY")

    onboarding_completed = models.BooleanField(default=False)

    birth_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name