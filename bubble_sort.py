again = "yes"
while again == "yes":
    nums = [int(x) for x in input("Enter numbers: ")]
    order = input("asc or desc: ")
    for _ in nums:
        for j in range(len(nums) - 1):
            if (order == "asc" and nums[j] > nums[j+1]) or (order == "desc" and nums[j] < nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print("Sorted:", nums)
    again = input("Sort again? (yes/no): ").lower()
print("Goodbye!")