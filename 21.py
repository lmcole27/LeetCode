#import icecream
from icecream import ic # type: ignore

nums = [4,3,2,7,8,2,3,1]
result = []

high = len(nums) + 1
n2 = list(set(nums))
print(nums, n2, len(nums))
#ic(nums, n2, len(nums))
for n in range(1,high):
    if n not in nums:
        result.append(n)
print(result)
#icecream.ic(result)
ic(result)





# if nums == []:
# #     return []
# low = nums[0]
# high = nums[0]

# for num in nums:
#     if num < low:
#         low = num
#       print(f"low = {low}")
#     if num > high:
#         high = num
#       print(f"low = {low}")
# for n in range(low, high):
#     if n not in nums:
#         result.append(n)
# print(result)