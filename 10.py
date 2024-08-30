# class Solution(object):

#   def moveZeroes(self, nums):
#     """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#     for i in range(len(nums), 0, -1):
#       if nums[i - 1] == 0:
#         nums.append(0)
#         del nums[i - 1]
#     return nums


# n = [1, 0, 3, 0, 12]
# print(Solution().moveZeroes(n))


a = [3,4,5,9,8,7]
b = [1,2,9,8,7]
c = [3,4,5,9,8,7,1,2,9,8,7]
d = [1,2,9,8,7,3,4,5,9,8,7]

# for x in c and for y in d:
#   if x == y:
#     print(x)
