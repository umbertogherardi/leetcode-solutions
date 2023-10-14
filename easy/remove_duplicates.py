class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_dups = 0
        original_len = len(nums)

        for i in range(len(nums)):
            duplicate_count = 0

            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    duplicate_count += 1
                    if (j == len(nums) - 1):
                        return original_len - (total_dups + duplicate_count)

                else:
                    if duplicate_count > 0:
                        nums[i + 1 :] = nums[i + 1 + duplicate_count : len(nums)]
                        total_dups += duplicate_count
                        break
        
        return original_len - total_dups
