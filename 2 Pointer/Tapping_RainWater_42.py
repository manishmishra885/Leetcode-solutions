class Solution:
    def trap(self, height: List[int]) -> int:
        # OPTIMAL SOLUTION----Dynamic Programming Approach ! 
         
        water = 0 
        n = len(height)
        if n == 0:
            return 0 

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range (1,n):
            left_max[i] = max (height[i], left_max[i-1])
        right_max[n-1] = height[n-1]
        for i in range (n-2,-1,-1):
            right_max[i] = max (height[i], right_max[i+1])
        for i in range (n):
            water += min (left_max[i],right_max[i]) - height[i]
        return water
        # MOST BRUTE FROCE APPROACH WOULD BE 
        '''water = 0 
        for i in range (len(height)):
            left_max = max (height[:i+1])
            right_max = max (height[i:])
            water += min (left_max,right_max) - height[i]
        return water''' 
