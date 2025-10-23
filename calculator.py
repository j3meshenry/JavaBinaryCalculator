# file: calculator.py
# author: James Henry (Python version)
# functionality: Takes two decimal inputs, adds them, and displays both decimal and binary (MSB-aligned) output.

def main():
    try:
        # User inputs
        num1 = int(input("Enter the first number (decimal): "))
        num2 = int(input("Enter the second number (decimal): "))

        # Perform addition
        total = num1 + num2

        # Determine max bit length for alignment
        max_bits = max(len(bin(num1)[2:]), len(bin(num2)[2:]))

        # Pad binary strings
        bin1 = format(num1, f'0{max_bits}b')
        bin2 = format(num2, f'0{max_bits}b')
        bin_sum = format(total, f'0{max_bits}b')

        # Output in decimal
        print("\n--- Decimal Output ---")
        print(f"First number: {num1}")
        print(f"Second number: {num2}")
        print(f"Sum: {total}")

        # Output in binary
        print("\n--- Binary Output (MSB aligned) ---")
        print(f"First number:  {bin1}")
        print(f"Second number: {bin2}")
        print(f"Sum:           {bin_sum}")

    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
