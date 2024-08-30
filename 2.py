class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      #Try 3
        sum = 0
        max_sum = max(nums)
        if max_sum < 0:
          return max_sum
          
        for i in range(len(nums)):          
          if sum + nums[i] > 0:
            sum += nums[i]
            if sum > max_sum:
              max_sum = sum
          else:
            sum = 0
        return max_sum


      # #Copied Solution
        # max_so_far = nums[0]
        # max_ending_here = 0
        # # start = 0
        # # end = 0
        # # s = 0
        # size = len(nums)    
        # for i in range(0, size):
     
        #     max_ending_here += nums[i]
     
        #     if max_so_far < max_ending_here:
        #         max_so_far = max_ending_here
        #         # start = s
        #         # end = i
     
        #     if max_ending_here < 0:
        #         max_ending_here = 0
                # s = i+1
        # return max_so_far
        # # print("Maximum contiguous sum is %d" % (max_so_far))
        # # print("Starting Index %d" % (start))
        # # print("Ending Index %d" % (end))


#nums = [1,-2,1,-3,4,-1,2,1,-5,4]     
nums = [5,4,-1,7,8]
#nums = [1]
#nums = [-1 , -4, -3 ,-9, -7]
x = Solution().maxSubArray(nums)
print(x)

      #TRY 2
        # max_sum = 0
        # first_num = 0
        # last_num = len(nums)-1
        # print(first_num, last_num)
        # for num in nums:
        #   max_sum += num
        # print(max_sum)
        # print(nums[first_num])
        # while max_sum - nums[first_num] > max_sum:
        #   max_sum -= nums[first_num]
        #   first_num += 1
        #   print(max_sum)
        # while max_sum - nums[last_num] > max_sum:
        #   max_sum -= nums[last_num]
        #   last_num -= 1
        # return max_sum


      #TRY 1
        # og_sum = nums[0]
        # first_num_i = 0
        # skip = False
        # # self.sub_array = {}
        # for i, v in enumerate(nums):
        #     if i== 0:
        #       # self.sub_array = {i, v}  
        #       continue
        #     print(i, v)
        #     new_sum = og_sum + v
        #     if skip == True and v > og_sum:
        #       og_sum = v
        #       first_num_i = i
        #       skip = False
        #       continue
        #     if new_sum > og_sum and skip == False:
        #       # self.sub_array = {i, v}  
        #       og_sum = new_sum
        #     else:
        #       skip = True          
        #     if new_sum - nums[first_num_i] > og_sum:
        #       og_sum = new_sum - nums[first_num_i]
        #       first_num_i += 1
        #     print(og_sum)
        # return og_sum
        

