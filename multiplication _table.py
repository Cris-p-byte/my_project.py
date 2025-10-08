choice = 'y'
while choice.lower() == 'y':
    num = int(input("Enter a number: "))
    
    print(f"\nMultiplication Table of {num}\n")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    
    choice = input("Do you want to generate another table? (y/n): ")

print("Thanks for using the program!")
