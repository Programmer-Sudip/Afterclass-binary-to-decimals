def binary_to_decimal(binary_str):
    """
    Convert a binary number (as a string) to a decimal number.

    :param binary_str: A string representing a binary number (e.g., '1101')
    :return: An integer representing the decimal equivalent of the binary number
    """
    decimal = 0
    length = len(binary_str)

    for i, digit in enumerate(binary_str):
        # Calculate the decimal value
        decimal += int(digit) * (2 ** (length - 1 - i))

    return decimal

def decimal_to_binary(decimal):
    """
    Convert a decimal number to a binary number (as a string).

    :param decimal: An integer representing a decimal number
    :return: A string representing the binary equivalent of the decimal number
    """
    if decimal == 0:
        return '0'

    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    return binary

def main():
    while True:
        print("Select conversion type:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            binary_str = input("Enter a binary number: ").strip()
            try:
                decimal_number = binary_to_decimal(binary_str)
                print(f"Binary to Decimal: {binary_str} -> {decimal_number}")
            except ValueError:
                print("Invalid input. Please enter a valid binary number.")

        elif choice == '2':
            decimal_str = input("Enter a decimal number: ").strip()
            try:
                decimal_number = int(decimal_str)
                binary_str = decimal_to_binary(decimal_number)
                print(f"Decimal to Binary: {decimal_number} -> {binary_str}")
            except ValueError:
                print("Invalid input. Please enter a valid decimal number.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()