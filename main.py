from bmi import calculate_bmi, get_category

def main():
    print("===== BMI CALCULATOR =====")

    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (meters): "))

        if weight <= 0 or height <= 0:
            print("Invalid input! Values must be positive.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()