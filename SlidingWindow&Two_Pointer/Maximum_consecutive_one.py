class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0 
        left = 0 
        maxo = 0 
        for right in range (len(nums)):
            if nums[right] == 0 :
                zero_count += 1 

            while zero_count > k :

                if nums[left] == 0:
                    zero_count -= 1
                left += 1 

            maxo = max (maxo , right - left + 1 )
        return maxo 