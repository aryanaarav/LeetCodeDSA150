class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}

        for i in range(len(nums)):
            if nums[i] not in table:
                table[(target-nums[i])] = i
            else:
                return [i, table[nums[i]]]