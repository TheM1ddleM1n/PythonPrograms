"""
Username Generator - Create usernames from your info
Enhanced with validation and multiple format options
"""

import re


def validate_name(name, field="name"):
    """Validate that name contains only letters, spaces, hyphens, and apostrophes."""
    if not name or not name.strip():
        raise ValueError(f"{field} cannot be empty")
    
    if not re.fullmatch(r"[A-Za-z\s\-']+", name):
        raise ValueError(f"{field} contains invalid characters")
    
    return name.strip()


def validate_year(year):
    """Validate year is a 4-digit number."""
    if not year.isdigit() or len(year) != 4:
        raise ValueError("Year must be exactly 4 digits")
    
    year_int = int(year)
    if year_int < 1900 or year_int > 2025:
        raise ValueError("Year must be between 1900 and 2025")
    
    return year


def generate_username(forename, surname, year, style="default"):
    """
    Generate username from personal information.
    
    Styles:
    - default: YYFLastname (e.g., 99JSmith)
    - full: FirstnameLastnameYY (e.g., JohnSmith99)
    - compact: FLLastYY (e.g., JSSmith99)
    - modern: firstname.lastname.YY (e.g., john.smith.99)
    """
    forename = forename.lower()
    surname = surname.lower()
    yy = year[2:4]
    
    styles = {
        "default": f"{yy}{forename[0]}{surname}",
        "full": f"{forename}{surname}{yy}",
        "compact": f"{forename[0]}{surname[0]}{surname}{yy}",
        "modern": f"{forename}.{surname}.{yy}",
        "reverse": f"{surname}{forename[0]}{yy}",
        "underscore": f"{forename}_{surname}_{yy}"
    }
    
    return styles.get(style, styles["default"])


def main():
    print("=" * 50)
    print("🆔 USERNAME GENERATOR")
    print("=" * 50)
    
    try:
        # Get user input with validation
        forename = input("Enter your first name: ")
        forename = validate_name(forename, "First name")
        
        surname = input("Enter your surname: ")
        surname = validate_name(surname, "Surname")
        
        year = input("Enter the year you were born (YYYY): ")
        year = validate_year(year)
        
        # Show all username styles
        print("\n" + "=" * 50)
        print("📝 GENERATED USERNAMES")
        print("=" * 50)
        
        styles = ["default", "full", "compact", "modern", "reverse", "underscore"]
        for i, style in enumerate(styles, 1):
            username = generate_username(forename, surname, year, style)
            print(f"{i}. {style.capitalize():12} → {username}")
        
        # Let user choose
        print("\n" + "=" * 50)
        choice = input("Choose a style (1-6) or press Enter for default: ").strip()
        
        if choice and choice.isdigit() and 1 <= int(choice) <= 6:
            selected_style = styles[int(choice) - 1]
        else:
            selected_style = "default"
        
        final_username = generate_username(forename, surname, year, selected_style)
        
        print("\n" + "=" * 50)
        print(f"✅ Your username is: {final_username}")
        print("=" * 50)
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled by user")


if __name__ == "__main__":
    main()
