class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = []
        for n in nums:
            if n in once:
              n_ind = once.index(n)
              del once[n_ind]
            else:
              once.append(n)
        return once[0]

x = [2,2, 1]
print(Solution().singleNumber(x))