class Solution(object):

  def missingNumber(self, nums):
    """
      :type nums: List[int]
      :rtype: int
      """
    nums.sort()
    for i in range(len(nums)):
      print(i)
      if nums[i] != i:
        return i
    return nums[-1] + 1

s = Solution()
print(s.missingNumber([3,0,1]))
