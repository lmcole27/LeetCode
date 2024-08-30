# class Solution():
#   def twoSum(self, nums, target):
#       for x in range(len(nums)):
#         for y in range(x+1,len(nums)):
#           if nums[x]+nums[y] == target:
#             return [x, y]

class Solution():
  def twoSum(self, nums, target):
      seen = {}
      for x in range(len(nums)):
        if target - nums[x] in seen:
          return [seen[target - nums[x]], x]
        seen[nums[x]] = x
      return []

# class Solution():
#   def twoSum(self, nums, target):
#         seen = {}
#         for i, v in enumerate(nums):
#           print(f"i ={i}, v={v}")
#           remaining = target - v
#           if remaining in seen:
#             return [seen[remaining], i]
#           seen[v] = i
#         return []

# class Solution:
#     def twoSum(self, nums, target):
#         numToIndex = {}
#         for i in range(len(nums)):
#             if target - nums[i] in numToIndex:
#                 return [numToIndex[target - nums[i]], i]
#             numToIndex[nums[i]] = i
#         return []

ret = Solution().twoSum(nums = [3,3], target = 6)
# y = Solution(nums = [3,3], target = 6)
# y.twoSum()
print(ret)