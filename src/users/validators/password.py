import re
from rest_framework.exceptions import ValidationError


def validate_password_strength(password: str):
    if len(password) < 8 or len(password) > 16:
        raise ValidationError("A senha deve ter entre 8 e 16 caracteres")

    if not re.search(r'[A-Z]', password):
        raise ValidationError("A senha deve conter pelo menos uma letra maiúscula")

    if not re.search(r'[a-z]', password):
        raise ValidationError("A senha deve conter pelo menos uma letra minúscula")

    if not re.search(r'\d', password):
        raise ValidationError("A senha deve conter pelo menos um número")

    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        raise ValidationError("A senha deve conter pelo menos um caractere especial")

    return password