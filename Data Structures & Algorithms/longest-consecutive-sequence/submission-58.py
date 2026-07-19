class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Remove duplicates and sort cleanly
        temp = sorted(list(set(nums)))
        
        max_streak = 1
        current_streak = 1
        
        for i in range(len(temp) - 1):
            # This single condition works for ALL numbers (positive, negative, and zero)
            if temp[i+1] - temp[i] == 1:
                current_streak += 1
            else:
                # We hit a gap! Save the record and reset the counter to 1
                max_streak = max(max_streak, current_streak)
                current_streak = 1
                
        # One final check in case the longest sequence goes all the way to the end
        return max(max_streak, current_streak)
