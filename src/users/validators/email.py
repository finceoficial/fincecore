import re
from rest_framework.exceptions import ValidationError

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'


def validate_email_format(email: str):
    email = email.lower().strip()

    if not re.match(EMAIL_REGEX, email):
        raise ValidationError("Email inválido")

    return email