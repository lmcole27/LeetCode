import string

# class Solution(object):
#   def reverseOnlyLetters(self, s):
#       """
#       :type s: str
#       :rtype: str
#       """
#       ans = ""
#       alpha = string.ascii_letters
#       l = list(s)
#       b_pointer = 0
#       e_pointer = -1
#       b_value = s[b_pointer]
#       e_value = s[e_pointer]

#       while b_pointer + abs(e_pointer) < len(s):
#           if l[b_pointer] not in alpha:
#             b_pointer += 1
#           if l[e_pointer] not in alpha:
#             e_pointer -=1
#           if l[b_pointer] in alpha and l[e_pointer] in alpha
#             b_value = s[b_pointer]
#             e_value = s[e_pointer]
#             l[b_pointer] = e_value
#             l[e_pointer] = b_value
#             b_pointer += 1
#             e_pointer -= 1
#       for v in l:
#         ans += v
#       return ans

#Speedier?
class Solution(object):
  def reverseOnlyLetters(self, s):
      """
      :type s: str
      :rtype: str
      """
      ans = ""
      alpha = string.ascii_letters
      l = list(s)
      b_pointer = 0
      e_pointer = -1
      b_value = s[b_pointer]
      e_value = s[e_pointer]

      while b_pointer + abs(e_pointer) < len(s):
          if l[b_pointer] in alpha:
            if l[e_pointer] in alpha:
              b_value = s[b_pointer]
              e_value = s[e_pointer]
              l[b_pointer] = e_value
              l[e_pointer] = b_value
              b_pointer += 1
              e_pointer -= 1
            else:
              e_pointer -=1
          else:
            b_pointer += 1
      for v in l:
        ans += v
      return ans


x = "ab-cd"
xi = "a-bC-dEf-ghIj"
xii = "Test1ng-Leet=code-Q!"

s = Solution()
print(s.reverseOnlyLetters(x))
print(s.reverseOnlyLetters(xi))
print(s.reverseOnlyLetters(xii))