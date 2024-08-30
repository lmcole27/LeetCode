class Solution(object):
  def sortedSquares(self, nums):
      """
      :type nums: List[int]
      :rtype: List[int]
      """
      square = []

      for n in nums:
          square.append(n**2)
      square.sort()
      return square

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

