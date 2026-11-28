class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        write_index = 0
        scout_index = 0
        max_loops = len(nums)

        for i in range(max_loops):
            if nums[write_index] != 0 and nums[scout_index] != 0:
                write_index += 1
                scout_index += 1
            elif nums[write_index] == 0 and nums[scout_index] == 0:
                scout_index += 1
            elif nums[write_index] == 0 and nums[scout_index] != 0:
                temp = nums[write_index]
                nums[write_index] = nums[scout_index]
                nums[scout_index] = temp
                write_index += 1
                scout_index += 1


if __name__ == "__main__":
    sol = Solution()

    # 1. Standard case (zeros at the start and in the middle)
    t1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(t1)
    assert t1 == [1, 3, 12, 0, 0]

    # 2. Single zero (minimal edge case)
    t2 = [0]
    sol.moveZeroes(t2)
    assert t2 == [0]

    # 3. Single non-zero element (no zeros at all)
    t3 = [1]
    sol.moveZeroes(t3)
    assert t3 == [1]

    # 4. Starts with non-zero elements (verifies initial pointer sync)
    t4 = [4, 2, 0, 5, 0]
    sol.moveZeroes(t4)
    assert t4 == [4, 2, 5, 0, 0]

    # 5. Consecutive zeros
    t5 = [0, 0, 1, 0, 0, 2]
    sol.moveZeroes(t5)
    assert t5 == [1, 2, 0, 0, 0, 0]

    # 6. Zeros already at the end (no swaps needed)
    t6 = [1, 2, 3, 0, 0]
    sol.moveZeroes(t6)
    assert t6 == [1, 2, 3, 0, 0]

    # 7. All zeros
    t7 = [0, 0, 0]
    sol.moveZeroes(t7)
    assert t7 == [0, 0, 0]

    # 8. Negative numbers (verifies != 0 handles negatives properly)
    t8 = [-1, 0, -5, 0, 3]
    sol.moveZeroes(t8)
    assert t8 == [-1, -5, 3, 0, 0]

    print("All tests passed successfully!")
