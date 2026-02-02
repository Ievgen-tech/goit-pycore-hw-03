"""Normalize phone numbers to international format."""

import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone number to standard international format.

    Parameters:
    phone_number (str): phone number in any format.

    Returns:
    str: normalized phone number with only digits and '+' at the start.
    """
    # Remove all characters except digits and '+'
    cleaned = re.sub(r'[^\d+]', '', phone_number)

    # Remove '+' from middle or end, keep only at start
    if '+' in cleaned:
        cleaned = '+' + cleaned.replace('+', '')

    # Add international code for Ukraine if missing
    if not cleaned.startswith('+'):
        if cleaned.startswith('380'):
            cleaned = '+' + cleaned
        else:
            cleaned = '+38' + cleaned

    return cleaned


# Test cases with Ukrainian numbers
raw_numbers = [
    "    +38(050)123-32-39",
    "     0503451234",
    "0.501112228",
    "(050)8889900",
    "38050-111-22-28",
    "38050 111 22 17   ",
    "+380501234567",
    "0671234567",
    "38(067)111-22-33",
]

# Example of use

print("Normalized phone numbers for SMS sending:")
for number in raw_numbers:
    normalized = normalize_phone(number)
    print(f"{number:30} -> {normalized}")
