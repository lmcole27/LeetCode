# n = 1
# pointer_a = 0
# s = "leletcodecteo"
# x = list(s)
# ans_list = []
# no_list = []

# while n < len(x):
#   print(pointer_a, x[pointer_a], n, x[n], no_list, ans_list)
#   if x[n] not in ans_list and x[n] not in no_list and x[n] != x[pointer_a]:
#     ans_list.append(x[n])
#   elif x[n] in ans_list:
#     ans_list.remove(x[n]) 
#     if x[n] not in no_list:
#       no_list.append(x[n])
#   if x[pointer_a] == x[n] and x[n] not in no_list:
#       no_list.append(x[n])
#   if x[pointer_a] in no_list:
#       if len(ans_list) > 0:
#         pointer_a = x.index(ans_list[0])
#         ans_list.pop(0)
#       else:
#         pointer_a += 1
#   n += 1

#print("The end return", pointer_a, x[pointer_a], ans_list, no_list)
  
# class Solution(object):
#   def firstUniqChar(self, s):
#       """
#       :type s: str
#       :rtype: int
#       """

#       n = 1
#       pointer_a = 0
#       x = list(s)
#       ans_list = []
#       no_list = []

#       while n < len(x):
#         print(pointer_a, x[pointer_a], n, x[n], no_list, ans_list)
#         if x[n] not in ans_list and x[n] not in no_list and x[n] != x[pointer_a]:
#             ans_list.append(x[n])
#         elif x[n] in ans_list:
#             ans_list.remove(x[n]) 
#             if x[n] not in no_list:
#               no_list.append(x[n])
#         if x[pointer_a] == x[n] and x[n] not in no_list:
#           no_list.append(x[n])
#           if x[pointer_a] in no_list:
#             if len(ans_list) > 0:
#                 pointer_a = x.index(ans_list[0])
#                 ans_list.pop(0)
#             else:
#               n += 1
#               pointer_a = n
#         n += 1
      
#       if pointer_a < len(x) and x[pointer_a] not in no_list:
#         return pointer_a
#       else:
#        return -1

# s = "aadadaad"
# solution = Solution()
# print(solution.firstUniqChar(s))

from collections import Counter

class Solution(object):
  def firstUniqChar(self, s):
      """
      :type s: str
      :rtype: int
      """
      counter = Counter(s)

      for c in s:
        if counter[c] == 1:
          return s.index(c)
      return -1


s = "aadadaadc"
solution = Solution()
print(solution.firstUniqChar(s))