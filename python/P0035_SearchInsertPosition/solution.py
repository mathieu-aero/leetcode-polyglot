class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        target_index = -1
        left = 0
        right = len(nums) - 1
        search_position_ongoing = True

        while left <= right and search_position_ongoing:
            center = (right + left) // 2
            if nums[center] > target:
                right = center - 1
            elif nums[center] < target:
                left = center + 1
            else:
                target_index = center
                search_position_ongoing = False

        if target_index == - 1:
            return left
        else:
            return target_index


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.searchInsert([1, 3, 5, 6], 7))
    print("All tests passed successfully!")
