import hashlib

def hash_value(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()