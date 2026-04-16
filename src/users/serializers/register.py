from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models.laywer import LawyerProfile

from ..validators.email import validate_email_format
from ..validators.password import validate_password_strength
from ..validators.cpf import validate_cpf as validate_cpf_format

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    full_name = serializers.CharField()
    cpf = serializers.CharField()
    oab_number = serializers.CharField()
    oab_state = serializers.CharField()

    def validate_email(self, value):
        value = validate_email_format(value)

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email já está em uso")

        return value

    def validate_password(self, value):
        return validate_password_strength(value)

    def validate_cpf(self, value):
        value = validate_cpf_format(value)

        if LawyerProfile.objects.filter(cpf=value).exists():
            raise serializers.ValidationError("CPF já está cadastrado")

        return value

    def create(self, validated_data):
        profile_data = {
            "full_name": validated_data.pop("full_name"),
            "cpf": validated_data.pop("cpf"),
            "oab_number": validated_data.pop("oab_number"),
            "oab_state": validated_data.pop("oab_state"),
        }

        from django.db import transaction, IntegrityError
        from rest_framework.exceptions import ValidationError

        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    email=validated_data["email"],
                    password=validated_data["password"]
                )

                LawyerProfile.objects.create(
                    user=user,
                    **profile_data
                )

                return user

        except IntegrityError:
            raise ValidationError({
                "detail": "Email ou CPF já cadastrados"
            })