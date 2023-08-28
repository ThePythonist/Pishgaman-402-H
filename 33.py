nums = [1, 2, 3, 4, 5]

for i in range(5):
    x = int(input("Enter any number :"))
    if 5 < x < 11:
        nums.append(x)

print(nums)

# while len(nums) != 10:
#     x = int(input("Enter any number :"))
#     if 5 < x < 11:
#         nums.append(x)
#
# nums.sort()
# print(nums)
