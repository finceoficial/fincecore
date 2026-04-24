from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, ValidationError

from src.expenses.models.expenses import Expense
from src.expenses.models.expenses_deferral import ExpenseDeferral
from src.expenses.serializers.expenses import ExpenseSerializer, ExpenseDeferralSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(
            firm__members__user=self.request.user
        )

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied("Authentication required")

        membership = user.firm_memberships.first()

        if not membership:
            raise ValidationError("User has no firm")

        serializer.save(firm=membership.firm)

    @action(detail=True, methods=["post"])
    def defer(self, request, pk=None):
        expense = self.get_object()

        serializer = ExpenseDeferralSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(
            expense=expense,
            original_date=expense.due_date
        )

        expense.due_date = serializer.validated_data["new_date"]
        expense.save()

        return Response(serializer.data)