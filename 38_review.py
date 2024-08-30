# # LeetCode38
# numbers = [3,24,50,79,88,150,345]
# target = 200
# k = 0
# print(len(numbers)-1)
# for i in range(len(numbers)-1):
#     if numbers[i-k]+numbers[i+1] > target:
#         k+=1
#     if numbers[i-k]+numbers[i+1] == target:
#         print([i+1-k,i+2])

# cost = [10,15,20]
# i = 0
# op_a = cost[-1]
# op_b = cost[-2]


# option1 = cost[i]+cost[i+1]
# option2 = cost[i]+cost[i+2]
# option3 = cost[i+1]
# cost = [1,100,1,1,1,100,1,1,100,1]
# print(sum(cost))
# print(sum(cost)/len(cost))
# ans = min((cost[0]+cost[1]), (cost[0]+cost[2]), cost[1])
# print(ans)


# ans1 = cost[-1]
# ans3 = cost[-2]
# i=3

# while i < len(cost): 
#     ans1 =(ans1 + cost[-i]) 
#     ans2 = (ans1 + cost[-i-1])
#     ans3 = (ans2 + cost[-i])
#     ans4 = (ans2 + cost[-i-1])
#     i = i + 2
#     ans1 = ans2 = ans3 =ans4 = min(ans1, ans2, ans3, ans4)
# return ans1

# ans1 = cost[-1]
# ans2 = cost[-2]
# i=2

# while i < len(cost): 

#     if cost[-i] < cost[-i-1]:
#         ans1 += cost[-i]
#         ans1 = min(ans1, ans2)
#         i+=1

#     else:
#         ans2 += cost[-i-1]
#         i+=2
# return min(ans1, ans2)


# i = 1
# ans = 0

# while i < len(cost):
#     if cost[-i] < cost[-i-1]:
#         ans += cost[-i]
#         i+=1
#     else:
#         ans+= cost[-i-1]
#         i+=2
# return ans

# words = ["hi", "today", "is", "going", "to", "be", "a", "good", "day"]

# # numbers = list(map(len, words))
# # print(numbers)

# new = list(map(lambda s: s + ("lll"), words))
# print(new)

