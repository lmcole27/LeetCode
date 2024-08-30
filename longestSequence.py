# class Solution(object):
#   def __init__(self, arr, difference):
#     self.arr = arr
#     self.difference = difference
    
  # def longestSubsequence(self, arr, difference):
  #       """
  #       :type arr: List[int]
  #       :type difference: int
  #       :rtype: int
  #       """

arr = [1,5,7,8,5,3,4,2,1]
difference = -2

if difference != 0:
  arr = list(dict.fromkeys(arr))

arr.sort()
length = (len(arr))
print(f" arr = {arr}, length = {length}")

master_list = []
for num in range(0, length-1, 1):
  new_list = [arr[num]]
  next_num = arr[num] + difference
  while arr.count(next_num) != 0:
    x = arr.index(next_num)
    new_list.append(arr[x])
    next_num += difference
  master_list.append(new_list)
print(master_list)

answer=0
answer_set=[]
for k in master_list:
  if (len(k)) > x:
    answer = len(k)
    answer_set = k
print(f"answer = {answer}, {answer_set}")