class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_loop = len(nums)
        total = 0
        left_total = 0
        pivot_index = -1
        k = 0
        searching_leftmost_pivot_index = True

        for i in range(max_loop):
            total += nums[i]

        while k < max_loop and searching_leftmost_pivot_index:
            right_total = total - left_total - nums[k]

            if left_total == right_total:
                searching_leftmost_pivot_index = False
                pivot_index = k
            else:
                left_total += nums[k]
                k += 1

        return pivot_index


if __name__ == "__main__":
    sol = Solution()

    # Standard case: pivot in the middle
    assert sol.pivotIndex([1, 7, 3, 6, 5, 6]) == 3, "Failed on standard case [1, 7, 3, 6, 5, 6]"

    # No pivot exists
    assert sol.pivotIndex([1, 2, 3]) == -1, "Failed when no pivot exists [1, 2, 3]"

    # Pivot at the leftmost index (index 0)
    assert sol.pivotIndex([2, 1, -1]) == 0, "Failed on leftmost pivot [2, 1, -1]"

    # Pivot at the rightmost index (last index)
    assert sol.pivotIndex([-1, 1, 2]) == 2, "Failed on rightmost pivot [-1, 1, 2]"

    # Multiple pivots exist: must return the leftmost one (index 0)
    assert sol.pivotIndex([0, 0, 0, 0]) == 0, "Failed on multiple pivots [0, 0, 0, 0]"

    # Single element array
    assert sol.pivotIndex([5]) == 0, "Failed on single element array [5]"

    # Negative numbers only
    assert sol.pivotIndex([-1, -1, -1, -1, -1, 0]) == 2, "Failed on negative numbers"

    # Empty array edge case
    assert sol.pivotIndex([]) == -1, "Failed on empty array []"

    print("All tests passed successfully!")
