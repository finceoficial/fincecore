from rest_framework import serializers
from ..models.case_payment import CasePaymentSchedule, CasePaymentSchedule
from ..models.case_structure import Case


class CasePaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasePaymentSchedule
        fields = ["id", "amount", "expected_date", "probability", "paid"]


class CaseSerializer(serializers.ModelSerializer):
    schedules = CasePaymentScheduleSerializer(many=True, required=False)

    class Meta:
        model = Case
        fields = [
            "id",
            "firm",
            "client_name",
            "title",
            "total_fee",
            "payment_type",
            "win_probability",
            "stage",
            "expected_close_date",
            "schedules",
            "created_at",
        ]
        read_only_fields = ["firm"]

    def create(self, validated_data):
        schedules_data = validated_data.pop("schedules", [])
        firm = self.context["request"].user.firm_memberships.first().firm

        case = Case.objects.create(firm=firm, **validated_data)

        for schedule in schedules_data:
            CasePaymentSchedule.objects.create(case=case, **schedule)

        return case