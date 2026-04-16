from rest_framework import serializers
from ..models.laywer import LawyerProfile

class LawyerProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawyerProfile
        fields = [
            "full_name",
            "phone",
            "oab_number",
            "oab_state",
            "cpf",
            "office_address",
            "bank_name",
            "bank_account",
            "practice_areas",
            "years_of_experience",
            "average_monthly_income",
            "average_monthly_expense",
            "financial_goal",
            "office_type",
            "income_variability",
            "goal_type",
            "birth_date"
        ]