from rest_framework import serializers
from src.expenses.models import Expense, ExpenseDeferral


class ExpenseDeferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseDeferral
        fields = ["id", "original_date", "new_date", "penalty_amount", "created_at"]


class ExpenseSerializer(serializers.ModelSerializer):
    deferrals = ExpenseDeferralSerializer(many=True, read_only=True)

    class Meta:
        model = Expense
        fields = [
            "id",
            "firm",
            "title",
            "description",
            "amount",
            "due_date",
            "frequency",
            "is_active",
            "deferrals",
            "created_at",
        ]
        read_only_fields = ["firm"]

    def create(self, validated_data):
        firm = self.context["request"].user.firm_memberships.first().firm
        return Expense.objects.create(firm=firm, **validated_data)