"""
Module for calculating the number of days between dates.
"""

from datetime import datetime

def days_difference(date: str) -> int:
    """
    Calculate the number of days between the given date and the current date.

    Parameters:
    date (str): A date string in the format 'YYYY-MM-DD'.

    Returns:
    int: The number of days from the given date to the current date. A negative number
         indicates the given date is in the future.

    Raises:
    ValueError: If the date string is not in the correct format or contains invalid date values.
    TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(date, str):
        raise TypeError("Input must be a string in the format 'YYYY-MM-DD'")

    try:
        # Convert the date string to a datetime object
        given_date = datetime.strptime(date, '%Y-%m-%d')
        # Get the current date
        current_date = datetime.today()
        # Calculate the difference in days
        difference = (current_date - given_date).days
        return difference
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date}'. Error: {e}") from e

# Example of use
print(days_difference("2022-02-24"))  # Date in the past War in Ukraine
print(days_difference("2027-02-24"))  # Future date (negative number)
