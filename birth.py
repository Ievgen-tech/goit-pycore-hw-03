"""Determine upcoming birthdays and adjust for weekends."""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    Get list of users with birthdays in the next 7 days (including today).

    If birthday falls on weekend, move congratulation to next Monday.

    Parameters:
    users (list): list of dictionaries with keys 'name' and 'birthday' (format 'YYYY.MM.DD').

    Returns:
    list: list of dictionaries with keys 'name' and 'congratulation_date' (format 'YYYY.MM.DD').
    """
    today = datetime.today().date()
    result = []

    for user in users:
        # Convert birthday string to date object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Get birthday in current year
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday already passed this year, use next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate difference in days
        days_until_birthday = (birthday_this_year - today).days

        # Check if birthday is within next 7 days (including today)
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Check if birthday falls on weekend
            weekday = congratulation_date.weekday()

            # If Saturday (5) or Sunday (6), move to Monday
            if weekday == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif weekday == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


# Test data
test_users = [
    {"name": "John Doe", "birthday": "1985.02.03"},
    {"name": "Jane Smith", "birthday": "1990.02.04"},
    {"name": "Alice Johnson", "birthday": "1988.02.08"},
    {"name": "Bob Brown", "birthday": "1992.02.09"},
    {"name": "Charlie Wilson", "birthday": "1987.02.02"},
    {"name": "Diana Davis", "birthday": "1991.02.06"},
    {"name": "Eve Martinez", "birthday": "1989.02.15"},
]

upcoming_birthdays = get_upcoming_birthdays(test_users)

print("Upcoming birthdays (next 7 days):")
print("=" * 50)
for person in upcoming_birthdays:
    print(f"{person['name']}: congratulate on {person['congratulation_date']}")
