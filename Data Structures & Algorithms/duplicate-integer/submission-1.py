class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        saved = []
        for i in nums:
            if i in saved:
                return True
            else:
                saved.append(i)

        return False
        