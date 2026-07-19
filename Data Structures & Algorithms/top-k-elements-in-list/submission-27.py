class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stats = {}

        # Loop through all elements exactly ONCE
        for number in nums:
            # If 'number' isn't in stats, get 0 and add 1. 
            # If it is, get the current count and add 1.
            stats[number] = stats.get(number, 0) + 1

        # Your sorting and slicing logic is already perfect!
        sorted_keys = sorted(stats.keys(), key=stats.get, reverse=True)
        return sorted_keys[:k]
