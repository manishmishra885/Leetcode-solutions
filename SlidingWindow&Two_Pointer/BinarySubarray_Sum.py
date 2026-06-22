class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #OPTIMAL SOLUTION
        def helper(x):
            if x < 0 :
                return 0


            left , curr_sum = 0, 0
            count = 0
            for right in range(len(nums)):
                curr_sum += nums[right]
                
                while curr_sum > x:
                    
                    curr_sum -= nums[left] 
                    left  += 1

                count += right - left + 1

            return count

        return helper(goal) - helper(goal-1)

        # #this is extreame BRUTE FORCE 
        # n = len(nums)
        # left = 0 
        # count = 0 
        # for i in range (n):
        #     cur_sum = 0 
        #     for right in range(i,n):
        #         cur_sum += nums[right]

        #         if cur_sum == goal:
        #             count += 1 
        # return count