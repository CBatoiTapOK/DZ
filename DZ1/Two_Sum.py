class Solution:
    def twoSum(self, nums, target):
        table = {}

        for i, num in enumerate(nums):

            if num not in table:

                table[num] = i

            if (target - num) in table.keys():

                if table[target-num] != i:

                    return [table[target-num],i]
