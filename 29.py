class Solution(object):
  def isPalindrome(self, x):
      """
      :type x: int
      :rtype: bool
      """
      xl = str(x)
      r = len(xl)//2
      p = 1
      
      for i in range(r):
          if xl[i] != xl[-p]:
              return False
          p+=1
      
      return True

s = Solution()
print(s.isPalindrome(12213))

