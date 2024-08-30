class Solution(object):
  def maxSlidingWindow(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: List[int]
      """
      arr = []
      ans = []
      for n in range(k):
        arr.append(nums[n])
      ans.append(max(arr))
      for i in range(k, len(nums)):
        arr.append(nums[i])
        del arr[0]
        m = max(arr)
        ans.append(m)
      return ans
    
nums = [1,3,-1,-3,5,3,6,7]

k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))