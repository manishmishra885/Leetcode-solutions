class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1 
        suffix = 1 
        n = len(nums)
        maxi = float("-inf")
        for i in range (n):
            if prefix == 0:
                prefix = 1
            if suffix == 0 :
                suffix = 1 
            
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]
            maxi = max(maxi , max(prefix , suffix))
        return maxi
# """ This is the brute force solution 

#         product_map = {}
#         maxi = float("-inf")
        
#         for i in range(len(nums)):
#             product=1
#             for j in range (i, len(nums)):
#                 product = product * nums[j]
#                 product_map[(i,j)] = product 
#                 maxi = max(product, maxi)
#         return maxi
#         """
   
    