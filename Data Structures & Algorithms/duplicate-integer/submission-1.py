class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for i,number in enumerate(nums):
            if number not in array:
                array.append(number)
                continue
            return True
        return False