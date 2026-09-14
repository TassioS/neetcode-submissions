class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        """seen = []
        for number in nums:
            if number in seen:
                return True
            seen.append(number)
        return False"""

