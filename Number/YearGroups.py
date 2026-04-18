"""Determine UK Key Stage from year group."""


def get_key_stage(year):
    """
    Map UK year group to Key Stage level.

    Key Stage mapping:
    - KS1: Years 1-2
    - KS2: Years 3-6
    - KS3: Years 7-9
    - KS4: Years 10-11
    - KS5: Years 12-13

    Args:
        year (int): Year group (1-13)

    Returns:
        str: Key Stage description
    """
    if 1 <= year <= 2:
        return "Key Stage 1"
    elif 3 <= year <= 6:
        return "Key Stage 2"
    elif 7 <= year <= 9:
        return "Key Stage 3"
    elif 10 <= year <= 11:
        return "Key Stage 4"
    elif 12 <= year <= 13:
        return "Key Stage 5"
    else:
        raise ValueError("Year group must be between 1 and 13")


def main():
    """Main entry point."""
    try:
        year = int(input("Enter your year group (1-13): "))
        stage = get_key_stage(year)
        print(f"You are in {stage}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
