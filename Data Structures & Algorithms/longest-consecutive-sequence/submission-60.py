class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in numSet:
            # Check if 'n' is the absolute start of a sequence
            if (n - 1) not in numSet:
                length = 1
                # Expand the sequence forward
                while (n + length) in numSet:
                    length += 1
                # Track the maximum length found
                longest = max(length, longest)
                
        return longest