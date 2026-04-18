"""Month validation utility."""


def valid_month(month):
    """
    Validate if a month number is between 1 and 12.

    Args:
        month (int): Month number to validate

    Returns:
        None: Prints validation result
    """
    if month > 0 and month < 13:
        print("Valid month!")
    else:
        print("Invalid!")


# Main program
valid_month(6)
