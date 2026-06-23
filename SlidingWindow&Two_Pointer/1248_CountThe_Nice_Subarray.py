class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(x):
            if x < 0 :
                return 0 
            
            count = 0 
            odd_count = 0 
            left = 0 

            for right in range (len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1

                while odd_count > x:
                    if nums[left] % 2 == 1 :
                        odd_count -= 1 
                    left += 1 
                count += right - left + 1 
            return count
        return helper(k) - helper (k-1)

