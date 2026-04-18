"""Arithmetic demonstrations — operators, casting, and real-world formulas."""

import random


def maths_demo(x, y):
    """Demonstrate core arithmetic operators."""
    print(f"\n{'=' * 40}")
    print(f"🔢 Operators Demo: {x} and {y}")
    print(f"{'=' * 40}")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} // {y} = {x // y}  (integer division)")
    print(f"{x} % {y} = {x % y}  (modulus)")
    print(f"{x} ** {y} = {x**y}  (exponent)")


def float_demo():
    """Demonstrate float input and multiplication."""
    print(f"\n{'=' * 40}")
    print("🔢 Float Demo")
    print(f"{'=' * 40}")
    num = float(input("Enter a number with a decimal place: "))
    print(f"{num} × 3 = {num * 3}")


def heart_flow_rate(volume, time):
    """Calculate the flow rate of the heart."""
    return volume / time


def volume_of_sphere(r):
    """Calculate the volume of a sphere."""
    return 4 / 3 * (3.14 * (r**3))


def real_world_demos():
    """Demonstrate real-world formula calculations."""
    print(f"\n{'=' * 40}")
    print("🫀 Heart Flow Rate")
    print(f"{'=' * 40}")
    volume = 330
    time = 4
    rate = heart_flow_rate(volume, time)
    print(f"Volume: {volume}ml, Time: {time}s")
    print(f"Flow rate: {rate} ml/s")

    print(f"\n{'=' * 40}")
    print("🔵 Volume of a Sphere")
    print(f"{'=' * 40}")
    try:
        r = int(input("Enter radius: "))
        print(f"Volume: {volume_of_sphere(r):.2f}")
    except ValueError:
        print("⚠️ Please enter a valid integer.")


def main():
    print("🔢 Arithmetic Demos")

    while True:
        print(f"\n{'=' * 40}")
        print("1. Operators demo (random numbers)")
        print("2. Operators demo (your numbers)")
        print("3. Float multiplication")
        print("4. Real-world formulas")
        print("5. Exit")
        print(f"{'=' * 40}")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            maths_demo(random.randint(1, 100), random.randint(1, 10))
        elif choice == "2":
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                maths_demo(x, y)
            except ValueError:
                print("⚠️ Please enter valid numbers.")
        elif choice == "3":
            float_demo()
        elif choice == "4":
            real_world_demos()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
