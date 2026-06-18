class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
#skip if duplicate  a 
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
#skip if duplicate b 
            for j in range (i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                l = j+1 
                r = n-1
                while l < r :
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s > target:
                        r -= 1 
                    
                    elif s < target:
                        l += 1 
                    
                    else :
                        res.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l+= 1 
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1 
                        l += 1 
                        r -= 1 
        return res
    
    # this above  is 2 pointer approach for the 4 sum problem and the below is the hash map approach for the same problem


