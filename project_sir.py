while True:
    choice = input("Do you want (odd/even): ")

    i = int(input("Enter Desired Number: "))
   
    while (choice == "odd" and i % 2 == 0) or (choice == "even" and i % 2 == 1):
        print(f"Please enter a {choice} number.")
        i = int(input("Enter Desired Number: "))

    x = 1
    n = 0

    while x <= i:
        if choice == "odd" and x % 2 == 1:
            print(x)
            n += x
        elif choice == "even" and x % 2 == 0:
            print(x)
            n += x
        x += 1

    print("Total:", n)

    repeat = input("Do you want to repeat it again? (yes/no): ")
    if repeat != "yes":
        print("Goodbye!")
        break