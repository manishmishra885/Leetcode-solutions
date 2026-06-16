class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        result =[]
        for i in nums :
            count[i] = count.get(i,0) + 1 
        for key,value in count.items():
            if value > (len(nums)//3):
                result.append(key)
        return result
        