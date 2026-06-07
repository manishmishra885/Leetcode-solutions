class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0) +1
        
        for key,value in counter.items():
            if value == 1 :
                return(key)
