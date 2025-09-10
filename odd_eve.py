while True:
    print("Choose an option:")
    print("1.Show Odd Numbers")
    print("2.Show Even Numbers")

    choice = input("Enter your choice (1 or 2):")

    if choice == "1":
        limit = int(input("Enter the limit number: "))
        print(f"Odd numbers from 1 to {limit}:")
        for num in range(1, limit + 1):
            if num % 2 != 0:
                print(num, end=" ")
        print()

    elif choice == "2":
        limit = int(input("Enter the limit number: "))
        print(f"Even numbers from 1 to {limit}:")
        for num in range(1, limit + 1):
            if num % 2 == 0:
                print(num, end=" ")
        print()

    else:
        print("Invalid choice! Please select 1 or 2.")

    again = input("Do you want to try again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
