repeat = "yes"

while repeat.lower() == "yes":
    print("Choice Conversion:")
    print("a. Decimal to Binary")
    print("b. Decimal to Octal")
    print("c. Decimal to Hexadecimal")

    choice = input("Enter your choice (a, b, or c): ")

    if choice == "a":
        n = int(input("Enter Decimal Number: "))
        result = ""
        while n > 0:
            result = str(n % 2) + result
            n = n // 2
        print("Binary:", result or "0")

    elif choice == "b":
        n = int(input("Enter Decimal Number: "))
        result = ""
        while n > 0:
            result = str(n % 8) + result
            n = n // 8
        print("Octal:", result or "0")

    elif choice == "c":
        n = int(input("Enter Decimal Number: "))
        hex_digits = "0123456789ABCDEF"
        result = ""
        while n > 0:
            result = hex_digits[n % 16] + result
            n = n // 16
        print("Hexadecimal:", result or "0")

    else:
        print("Invalid choice! Please choose a, b, or c.")

    repeat = input("Do you want to convert again? (yes/no): ")
