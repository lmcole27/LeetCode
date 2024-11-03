import time as t
#print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start = str(t.time())
        function()
        finish = str(t.time())
        print(f"{function.__name__}: Elapsed Time = {float(finish)-float(start)}")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i*i

@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        i+i


fast_function()
slow_function()

# def slow_function():
#     y = current_time
#     x = current_time
#     return print(f"Elapsed Time = {x-y}")

# DECORATOR FUNCTION
# import time 

# def delay_fun(function):
#     def wrapper_function():
#         function()
#         time.sleep(2)
#         function()
#         function()
#         print("Goodbye")
#     return wrapper_function

# @delay_fun
# def hello():
#     print("hello")


# hello()



# import math
# print(dir(math))



# # importing the module
# import sys
       
# # fetching the maximum value
# max_val = sys.maxsize
 
# try:
 
#     # creating list with max size + 1
#     list = range(max_val)
 
#     # displaying the length of the list
#     print(len(list))
#     print("List successfully created")
     
# except Exception as e:
 
#     # displaying the exception
#     print(e)
#     print("List creation unsuccessful")

    
# code
#import sys
 
# # O(n * k) solution for finding
# # maximum sum of a subarray of size k
# INT_MIN = -sys.maxsize - 1
 
# # Returns maximum sum in a
# # subarray of size k.
 
 
# def maxSum(arr, n, k):
 
#     # Initialize result
#     max_sum = INT_MIN
 
#     # Consider all blocks
#     # starting with i.
#     for i in range(n - k + 1):
#         current_sum = 0
#         for j in range(k):
#             current_sum = current_sum + arr[i + j]
 
#         # Update result if required.
#         max_sum = max(current_sum, max_sum)
 
#     return max_sum
 

# def maxSum(arr, k):
#     n = len(arr)
#     cur_sum = sum(arr[:k])
#     max_sum = cur_sum
#     max_ind = 0

#     for i in range(k,n):
#         cur_sum = cur_sum - arr[i-4] + arr[i]
#         if cur_sum > max_sum:
#             max_sum = cur_sum
#             max_ind = i
#         print(i, max_sum, cur_sum)
#     return max_sum, f"{max_ind-k}:{max_ind}"
    

# # Driver code
# arr = [1, 4, 2, 10, 2,
#        3, 1, 0, 20]
# k = 4

# print(maxSum(arr, k))
