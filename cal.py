import math
import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename="logs/calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------------
# Scientific Functions
# ------------------------

def calculate_sqrt(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number.")
    result = math.sqrt(x)
    logging.info(f"sqrt({x}) = {result}")
    return result


def calculate_factorial(x):
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = math.factorial(x)
    logging.info(f"factorial({x}) = {result}")
    return result


def calculate_log(x):
    if x <= 0:
        raise ValueError("Logarithm defined only for positive numbers.")
    result = math.log(x)
    logging.info(f"log({x}) = {result}")
    return result


def calculate_power(x, y):
    result = math.pow(x, y)
    logging.info(f"power({x}, {y}) = {result}")
    return result


# ------------------------
# Menu Interface
# ------------------------

def menu():
    while True:
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Log (ln)")
        print("4. Power (x^y)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                num = float(input("Enter number: "))
                print("Result:", calculate_sqrt(num))

            elif choice == "2":
                num = int(input("Enter number: "))
                print("Result:", calculate_factorial(num))

            elif choice == "3":
                num = float(input("Enter number: "))
                print("Result:", calculate_log(num))

            elif choice == "4":
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print("Result:", calculate_power(base, exponent))

            elif choice == "5":
                print("Exiting calculator...")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            logging.error(str(e))
            print("Error:", e)


if __name__ == "__main__":
    menu()

