from rest_framework import serializers
from ..models.firm_member import FirmMember
from ..models.firm_structure import Firm


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ["id", "name", "type", "created_at"]


class FirmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ["id", "name", "type"]

    def create(self, validated_data):
        user = self.context["request"].user

        firm = Firm.objects.create(**validated_data)

        FirmMember.objects.create(
            firm=firm,
            user=user,
            role=FirmMember.Role.OWNER
        )

        return firm


class FirmMemberSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = FirmMember
        fields = ["id", "user", "user_email", "role", "created_at"]