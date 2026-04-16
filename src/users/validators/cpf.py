import re
from rest_framework.exceptions import ValidationError


def validate_cpf(cpf: str):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        raise ValidationError("CPF deve ter 11 dígitos")

    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido")

    def calculate_digit(cpf_part):
        total = sum(int(num) * weight for num, weight in zip(cpf_part, range(len(cpf_part)+1, 1, -1)))
        digit = (total * 10) % 11
        return digit if digit < 10 else 0

    if calculate_digit(cpf[:9]) != int(cpf[9]):
        raise ValidationError("CPF inválido")

    if calculate_digit(cpf[:10]) != int(cpf[10]):
        raise ValidationError("CPF inválido")

    return cpf