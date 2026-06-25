class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #OPTIMAL APPROACH 
        '''optimal samajh nhi aaya , toh brute force he lagao'''




        # # BRUTE FORCE APPROACH where we use extra memory 
        # s = set()
        # for num in nums:
        #     if num > 0 :
        #         s.add(num)
        # for i in range (1,len(nums)+2):
        #     if i not in s :
        #         return i 