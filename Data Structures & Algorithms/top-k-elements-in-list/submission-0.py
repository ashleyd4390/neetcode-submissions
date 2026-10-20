class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # sort frequency hash
        sorted_freq = dict(sorted(freq_dict.items(), key=lambda item: item[1]))
        iter_sorted = list(reversed(sorted_freq.keys()))
        result = []
        for i in range(0,k):
            result.append(iter_sorted[i])
        return result