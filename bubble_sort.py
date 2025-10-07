num = input("Enter numbers: ")
order = input("asc or desc: ")

numbers = [int(x) for x in num]

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if order == "asc" and numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        elif order == "desc" and numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted:", numbers)