class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        val_count = nums.count(val)

        i = 0

        while i < len(nums):
            if (val_count == 0):
                return len(nums) - nums.count(val)
            
            elif nums[i] == val:
                nums.append(nums[i])
                nums[i:] = nums[i+1:]
                val_count -= 1
                i -= 1

            i += 1
