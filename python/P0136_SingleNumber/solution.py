class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        max_loop = len(nums)

        for i in range(max_loop):
            result ^= nums[i]

        return result


if __name__ == "__main__":
    sol = Solution()

    # Example 1: single element at the end
    assert sol.singleNumber([2, 2, 1]) == 1, "Failed on [2, 2, 1]"

    # Example 2: single element at the beginning
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4, "Failed on [4, 1, 2, 1, 2]"

    # Example 3: single element array
    assert sol.singleNumber([1]) == 1, "Failed on [1]"

    # Negative numbers only
    assert sol.singleNumber([-1, -1, -2]) == -2, "Failed on negative numbers"

    # Mix of positive, negative, and zero
    assert sol.singleNumber([-3, 0, 5, -3, 5]) == 0, "Failed on zero as single number"
    assert sol.singleNumber([0, 0, -7]) == -7, "Failed on negative single number with zeros"

    print("All tests passed successfully!")
