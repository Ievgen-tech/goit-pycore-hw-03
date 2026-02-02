"""Generate unique lottery numbers within a given range."""

from random import sample


# pylint: disable=redefined-builtin
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Return a sorted list of unique random numbers in the given range.

    Parameters:
    min (int): minimum possible number (at least 1).
    max (int): maximum possible number (at most 1000).
    quantity (int): how many numbers to pick (between min and max).

    Returns:
    list[int]: sorted list of unique numbers, or an empty list for invalid input.
    """
    if min < 1 or max > 1000 or min > max:
        return []

    if quantity < min or quantity > max:
        return []

    if quantity > (max - min + 1):
        return []

    numbers = sample(range(min, max + 1), quantity)
    return sorted(numbers)

# Example of use
lottery_numbers = get_numbers_ticket(1, 200, 8)
print("Your lottery numbers are:", lottery_numbers)
