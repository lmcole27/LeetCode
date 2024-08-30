class Solution(object):

  def climbStairs(self, n):
    """
        :type n: int
        :rtype: int
        """

    if n == 1:
      return 1
    if n == 2:
      return 2
    else:
      return Solution().stairs(n, 3, 2, 1)

  def stairs(self, n, x, n1, n2):
    if n == x:
      return n1 + n2
    else:
      x += 1
      temp = n1
      n1 = n1 + n2
      n2 = temp
      return Solution().stairs(n, x, n1, n2)

