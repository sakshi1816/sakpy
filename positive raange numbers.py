list1 = [12, -7, 5, 64, -14]
print("Input: list1 =", list1)
print("Output:", end=" ")
for num in list1:
    if num > 0:
        print(num, end=", ")
print("\b\b")  # to remove the last comma and space


list2 = [12, 14, -95, 3]
print("\nInput: list2 =", list2)
positive_nums = []
for num in list2:
    if num > 0:
        positive_nums.append(num)
print("Output:", positive_nums)
