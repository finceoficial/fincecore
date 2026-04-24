from datetime import date, timedelta
from decimal import Decimal

from src.expenses.models import Expense
from src.cases.models import CasePaymentSchedule


class CashflowService:
    @staticmethod
    def get_projection(firm, days=60):
        today = date.today()
        end_date = today + timedelta(days=days)

        expenses = Expense.objects.filter(
            firm=firm,
            due_date__lte=end_date,
            is_active=True
        )

        incomes = CasePaymentSchedule.objects.filter(
            case__firm=firm,
            expected_date__lte=end_date,
            paid=False
        )

        timeline = []

        current_date = today

        while current_date <= end_date:
            daily_income = Decimal("0")
            daily_expense = Decimal("0")

            for inc in incomes:
                if inc.expected_date == current_date:
                    daily_income += inc.amount * Decimal(str(inc.probability))

            for exp in expenses:
                if exp.due_date == current_date:
                    daily_expense += exp.amount

            timeline.append({
                "date": current_date,
                "income": daily_income,
                "expense": daily_expense,
                "balance": daily_income - daily_expense
            })

            current_date += timedelta(days=1)

        return timeline

    @staticmethod
    def get_summary(firm):
        expenses = Expense.objects.filter(firm=firm, is_active=True)
        incomes = CasePaymentSchedule.objects.filter(case__firm=firm, paid=False)

        total_expense = sum([e.amount for e in expenses], Decimal("0"))
        total_income = sum([
            i.amount * Decimal(str(i.probability)) for i in incomes
        ], Decimal("0"))

        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "net": total_income - total_expense
        }