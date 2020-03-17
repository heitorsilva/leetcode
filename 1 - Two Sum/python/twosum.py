class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 0 or nums == None:
            return []

        hashmap = {}

        for i, number in enumerate(nums):
            complement = target - number

            i2 = hashmap.get(complement, None)

            if i2 is not None:
                return [i2, i]

            hashmap[number] = i

        return []
