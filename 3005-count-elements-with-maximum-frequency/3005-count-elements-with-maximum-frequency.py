class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counters=Counter(nums)
        max_counts=max(counters.values())
        list_nb=[key for key,value in counters.items() if value==max_counts]
        return len(list_nb)*max_counts
        