class Solution(object):
  def isHappy(self, n):
      """
      :type n: int
      :rtype: bool
      """
      ans_list = [n]
      if n == 1:
        return True
      return self.isHappyHelper(n, ans_list)
    
  def isHappyHelper(self, n, ans_list):
      digits = [int(d)**2 for d in str(n)]
      ans = sum(digits)
      if ans == 1:
        return True
      if ans not in ans_list:
        ans_list.append(ans)
        return self.isHappyHelper(ans, ans_list)
      return False

s = Solution()
print(s.isHappy(2))
print(s.isHappy(1111111))


        