import random

from .string_tools import generate_random_string


def get_random_email(domain: str = "yandex.ru") -> str:
    return f"{generate_random_string(random.randint(12, 20))}@{domain}"