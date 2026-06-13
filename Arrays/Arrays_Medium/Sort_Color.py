class Solution:
    def sortColors(self, nums):
        # Step 1: Count occurrences using dict.get()
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Overwrite nums in sorted order
        index = 0
        for color in [0, 1, 2]:
            for i in range(count.get(color, 0)):
                nums[index] = color
                index += 1