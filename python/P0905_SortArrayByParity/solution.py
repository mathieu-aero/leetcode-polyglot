class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = 0
        right = len(nums)-1

        while left <= right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
            elif nums[left] % 2 == 0 and nums[right] % 2 != 0:
                left += 1
                right -= 1
            elif nums[left] % 2 == 0 and nums[right] % 2 == 0:
                left += 1
            elif nums[left] % 2 != 0 and nums[right] % 2 != 0:
                right -= 1
        return nums


if __name__ == "__main__":
    sol = Solution()

    # 1. Standard case (mixed odd and even numbers)
    assert sol.sortArrayByParity([3, 1, 2, 4]) == [4, 2, 2, 4] or sol.sortArrayByParity([3, 1, 2, 4]) == [4, 2, 1, 3]

    # Note: To match your exact two-pointer output deterministically:
    assert sol.sortArrayByParity([3, 1, 2, 4]) == [4, 2, 1, 3]

    # 2. Single zero (minimal even edge case)
    assert sol.sortArrayByParity([0]) == [0]

    # 3. Single odd element
    assert sol.sortArrayByParity([7]) == [7]

    # 4. Already sorted by parity (evens first, odds last)
    assert sol.sortArrayByParity([2, 4, 1, 3]) == [2, 4, 1, 3]

    # 5. All even numbers
    assert sol.sortArrayByParity([2, 4, 6, 8]) == [2, 4, 6, 8]

    # 6. All odd numbers
    assert sol.sortArrayByParity([1, 3, 5, 7]) == [1, 3, 5, 7]

    # 7. Even and odd numbers at the boundaries (left even, right odd)
    assert sol.sortArrayByParity([2, 3, 5, 4]) == [2, 4, 5, 3]

    print("All tests passed successfully!")
