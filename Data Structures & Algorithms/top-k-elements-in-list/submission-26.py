class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique=set(nums)
        stats={}

        for number in unique:
            count=0
            for j in range(len(nums)):
                    if number == nums[j]:
                        count+=1
            stats.update({number:count})

        sorted_keys = sorted(stats.keys(), key=stats.get, reverse=True)
        return sorted_keys[:k]


                
        