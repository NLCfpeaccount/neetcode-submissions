class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        new = []
        i = 0
             
        while i < len(nums):
            product = 1 
            
            # Create a FRESH, clean copy of nums every single time the loop runs
            temp = nums.copy() 
            
            # Safely pop from the copy without touching the original data
            temp.pop(i)

            for j in range(len(temp)):
                 product *= temp[j]
            
            new.append(product)
            i += 1
            
        return new