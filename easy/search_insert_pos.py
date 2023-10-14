class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        middle = len(nums) // 2
        end = len(nums) - 1

        last_valid_middle = 0

        while (start <= end):
            print(f"Middle: {middle}")
            if nums[middle] == target:
                return middle
                
            elif (nums[middle] > target):
                if (middle - 1 < start):
                    last_valid_middle = middle
                end = middle - 1

            else:
                if (middle + 1 > end):
                    last_valid_middle = middle
                start = middle + 1

            middle = (end - start) // 2 + start


        if (nums[last_valid_middle] > target):
            return last_valid_middle
        else: 
            return last_valid_middle + 1
    