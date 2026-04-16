import re

def normalize_email(email: str):
    return email.strip().lower()

def normalize_cpf(cpf: str):
    return re.sub(r"\D", "", cpf)

def normalize_phone(phone: str):
    return re.sub(r"\D", "", phone)