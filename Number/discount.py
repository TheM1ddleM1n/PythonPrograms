# 💸 Interactive Discount Calculator

# Constant for default discount rate
DEFAULT_DISCOUNT_RATE = 50


# 🧮 Subroutine to calculate the discounted price
def calculate_discounted_price(total_price, discount_rate):
    """
    Returns the price after applying the discount rate.
    """
    discount_amount = total_price * (discount_rate / 100)
    return total_price - discount_amount


# 🎬 Main Program
try:
    original_price = float(input("Enter the original price (£): "))

    # Let the user choose to use default or custom discount rate
    use_custom_rate = (
        input(f"Use default discount rate ({DEFAULT_DISCOUNT_RATE}%)? [Y/n]: ")
        .strip()
        .lower()
    )

    if use_custom_rate == "n":
        discount_rate = float(input("Enter your custom discount rate (%): "))
    else:
        discount_rate = DEFAULT_DISCOUNT_RATE

    final_price = calculate_discounted_price(original_price, discount_rate)

    print("\n--- Receipt ---")
    print(f"Original Price: £{original_price:.2f}")
    print(f"Discount Rate: {discount_rate}%")
    print(f"Final Price: £{final_price:.2f}")

except ValueError:
    print("⚠️ Please enter valid numerical values.")
