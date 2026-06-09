class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        result = 0 
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0) + 1
        
        maxi = max(counter.values())
        for key, value in counter.items():
            if value == maxi :
                return (key)
            
        

        