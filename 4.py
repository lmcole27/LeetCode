class Solution(object):
    stack = []
    bracket = {")":"(",  "]":"[", "}":"{"}
  
    def isValid(self, s):
      for c in s:
        if c in "({[":
          self.stack.append(c)
        elif not self.stack:
          return False
        elif self.bracket[c] == self.stack[-1]:
          del self.stack[-1]
        else:
          return False
          
      return bool(not self.stack)
          
s = "{[]}"
x = Solution().isValid(s)
print(x)

#TRY 2
    # o_bracket = ["(", "[", "{"]
    # c_bracket = [")", "]", "}"]  
    # def isValid(self, s):
    #     s_list = list(s)
    #     # new_list = []
    #     # for b in s_list:
    #     #   if b in self.o_bracket or b in self.c_bracket:
    #     #     new_list.append(b)
    #     return Solution().isValid2(s_list)
   
    # def isValid2(self, new_list):              
    #     if new_list == []:
    #       return True
    #     if new_list[0] in self.c_bracket:
    #       return False
    #     for x in new_list:
    #       print(x)
    #       if x in self.c_bracket:
    #         c_index = self.c_bracket.index(x)
    #         x_index = new_list.index(x)
    #         print(x_index)
    #         print(self.o_bracket[c_index])
    #         print(new_list[x_index - 1])
    #         if self.o_bracket[c_index] == new_list[x_index - 1]:
    #           print(new_list)
    #           del new_list[x_index-1]
    #           del new_list[x_index-1]
    #           print(new_list)
    #           return Solution().isValid2(new_list)
    #         else:
    #           return False
    #     return False
            
#Try 1
        # for x in s_list:
        #   if x in o_bracket or x in c_bracket:
        #     new_list.append(x)
        # print(new_list)
        # if new_list == []:
        #   return True
        # if c_bracket[0] in new_list or c_bracket[1] in new_list or c_bracket[2] in new_list:
        #   pass
        # else: 
        #   return False
          
        # for x in new_list:
        #   x_index = new_list.index(x)
        #   print(x_index, x)
        #   print(new_list)
        #   if x in c_bracket:
        #     c_index = c_bracket.index(x)
        #     print(c_index)
        #     if o_bracket[c_index] == new_list[x_index - 1]:
        #       del new_list[x_index-1]
        #       del new_list[x_index-1]
        #     else:
        #       return False


          
#s = "abcdef"
# s = "(]"
# x = Solution().isValid(s)
# print(x)

