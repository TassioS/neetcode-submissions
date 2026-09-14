class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNum = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dictNum:
                return [dictNum.get(difference),i]
            dictNum[nums[i]] = i